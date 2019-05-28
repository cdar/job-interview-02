from django.core.exceptions import ValidationError
from django import forms

from secureaccess.models import Element


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['file', 'url']

    def clean(self):
        super().clean()
        if self.is_valid():
            file = self.cleaned_data.get('file')
            url = self.cleaned_data.get('url')
            if file and url:
                raise ValidationError('Two parameters given, only one allowed - file or url.')
            if not file and not url:
                raise ValidationError('Missing parameters - file or url.')


class ElementPasswordForm(forms.Form):
    password = forms.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        """Parameter instance is required."""
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

    def clean_password(self):
        super().clean()
        if not self.instance.check_password(self.cleaned_data['password']):
            raise ValidationError('Bad password.')
        return self.cleaned_data['password']
