from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import RedirectView, CreateView, FormView

from secureaccess.forms import ElementForm, ElementPasswordForm
from secureaccess.models import Element


class IndexView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        self.pattern_name = 'add_element' if self.request.user.is_authenticated else 'login'
        return super().get_redirect_url(*args, **kwargs)


class AddElementView(LoginRequiredMixin, CreateView):
    form_class = ElementForm
    model = Element
    template_name = 'add_element.html'

    def form_valid(self, form):
        new_element = form.save(commit=False)
        raw_password = new_element.make_random_password()
        new_element.save()

        messages.add_message(self.request, messages.SUCCESS, new_element.shareable_link, extra_tags='sec1')
        messages.add_message(self.request, messages.SUCCESS, raw_password, extra_tags='sec2')

        return HttpResponseRedirect(reverse('element_added'))


class RequestElementView(FormView):
    form_class = ElementPasswordForm
    template_name = 'request_element.html'

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        element = Element.get_valid_obj(self.kwargs['uuid'])
        if element is None:
            raise Http404()
        form_kwargs['instance'] = element
        return form_kwargs

    def form_valid(self, form):
        element = form.instance

        if element.url:
            redirect_url = element.url
        else:
            redirect_url = element.file.url

        element.update_accessed()

        return HttpResponseRedirect(redirect_url)
