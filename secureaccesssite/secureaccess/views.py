from django.views.generic import RedirectView, TemplateView


class IndexView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        self.pattern_name = 'add_element' if self.request.user.is_authenticated else 'login'
        return super().get_redirect_url(*args, **kwargs)


class AddElementView(TemplateView):
    template_name = "add_element.html"
