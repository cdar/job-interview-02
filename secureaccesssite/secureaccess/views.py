from django.views.generic import RedirectView, CreateView

from secureaccess.forms import ElementForm
from secureaccess.models import Element


class IndexView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        self.pattern_name = 'add_element' if self.request.user.is_authenticated else 'login'
        return super().get_redirect_url(*args, **kwargs)


class AddElementView(CreateView):
    form_class = ElementForm
    model = Element
    template_name = "add_element.html"

