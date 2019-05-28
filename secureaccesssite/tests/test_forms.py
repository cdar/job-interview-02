from unittest import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase as DjangoTestCase

from secureaccess.forms import ElementForm, ElementPasswordForm
from secureaccess.models import Element


class TestElementForm(TestCase):

    def test_no_parameters(self):
        form = ElementForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('Missing parameters - file or url', form.errors.as_text())

    def test_two_parameters(self):
        form = ElementForm(data={'url': 'fff.pl'}, files={'file': SimpleUploadedFile('asdf.pdf', b'asdf')})
        self.assertFalse(form.is_valid())
        self.assertIn('Two parameters given, only one allowed', form.errors.as_text())

    def test_url(self):
        form = ElementForm(data={'url': 'fff.pl'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['url'], 'http://fff.pl')

    def test_file(self):
        form = ElementForm(files={'file': SimpleUploadedFile('asdf.pdf', b'weekend')})
        self.assertTrue(form.is_valid())
        file = form.cleaned_data['file']
        self.assertEqual('asdf.pdf', file.name)
        self.assertEqual(b'weekend', file.read())


class TestElementPasswordForm(DjangoTestCase):

    def test_correct_password(self):
        element = Element()
        element.set_password('dog')
        element.save()
        form = ElementPasswordForm(data={'password': 'dog'}, instance=element)
        self.assertTrue(form.is_valid())

    def test_bad_password(self):
        element = Element()
        element.set_password('cat')
        element.save()
        form = ElementPasswordForm(data={'password': 'dog'}, instance=element)
        self.assertFalse(form.is_valid())
        self.assertIn('Bad password', form.errors.as_text())
