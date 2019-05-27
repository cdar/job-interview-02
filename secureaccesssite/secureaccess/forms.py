from django.core.exceptions import ValidationError
from django.forms import ModelForm

from secureaccess.models import Element


class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = ['file', 'url']

    def clean(self):
        super().clean()
        if self.is_valid():
            file = self.cleaned_data.get('file')
            url = self.cleaned_data.get('url')
            if file and url:
                raise ValidationError(
                    'Two parameters given, only one allowed - file or url.'
                )
            if not file and not url:
                raise ValidationError(
                    'Missing parameters - file or url.'
                )


