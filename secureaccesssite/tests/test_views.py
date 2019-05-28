from unittest.mock import Mock

from django.contrib.auth import get_user_model
from django.http import Http404
from django.test import TestCase as DjangoTestCase
from django.urls import reverse

from secureaccess.forms import ElementForm
from secureaccess.models import Element
from secureaccess.views import RequestElementView


class TestAddElementView(DjangoTestCase):

    def test_login_required(self):
        response = self.client.get(reverse('add_element'))
        self.assertRedirects(
            response,
            '%s?next=%s' % (reverse('login'), reverse('add_element')),
            302
        )

    def test_get_response(self):
        user = get_user_model().objects.create_user('user', password='pass')
        self.client.login(username=user.username, password='pass')
        response = self.client.get(reverse('add_element'))
        content = str(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Add element', content)
        self.assertIn('enctype="multipart/form-data"', content)
        self.assertTrue(isinstance(response.context['form'], ElementForm))

    def test_element_creation_in_post(self):
        user = get_user_model().objects.create_user('user', password='pass')
        self.client.login(username=user.username, password='pass')
        self.assertEqual(Element.objects.count(), 0)
        response = self.client.post(reverse('add_element'), {'url': 'wiki.com'}, follow=True)
        self.assertRedirects(response, reverse('element_added'), 302)
        self.assertEqual(Element.objects.count(), 1)
        element = Element.objects.first()
        self.assertIsNotNone(element)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 2)
        self.assertIn('sec1', messages[0].tags)
        self.assertEqual(str(element.shareable_link), messages[0].message)
        self.assertIn('sec2', messages[1].tags)
        self.assertTrue(element.check_password(messages[1].message))
        content = str(response.content)
        self.assertIn(messages[1].message, content)


class TestRequestElementView(DjangoTestCase):

    def test_get_form_kwargs(self):
        element = Element.objects.create()
        uuid = str(element.shareable_link)
        reversed_uuid = uuid[::-1]
        self.assertNotEqual(uuid, reversed_uuid)
        view = RequestElementView()
        view.kwargs = {'uuid': reversed_uuid}
        view.request = Mock()
        self.assertRaises(Http404, view.get_form_kwargs)
        view.kwargs['uuid'] = uuid
        self.assertEqual(element, view.get_form_kwargs()['instance'])

    def test_form_valid(self):
        element = Element.objects.create(url='earth.com')
        self.assertFalse(element.accessed)
        view = RequestElementView()
        view.kwargs = {'uuid': str(element.shareable_link)}
        form = Mock(instance=element)
        response = view.form_valid(form)
        self.assertEqual(response.url, element.url)
        element.refresh_from_db()
        self.assertTrue(element.accessed)
