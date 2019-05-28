from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from django.db import models

from secureaccess.forms import ElementForm
from secureaccess.models import Element, UserProfile


class UserProfileInline(admin.StackedInline):
    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea(attrs={'rows': 4, 'cols': 100})},
    }

    model = UserProfile
    can_delete = False


class UserAdmin(DjangoUserAdmin):
    inlines = [UserProfileInline]
    pass


class ElementFormAdmin(ElementForm):
    new_password = forms.CharField(max_length=128, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['size'] = 100

    class Meta:
        model = Element
        exclude = []

    def save(self, commit=True):
        new_password = self.cleaned_data.get('new_password')
        self.instance.set_password(new_password)
        return super().save(commit)


class ElementAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, change=False, **kwargs):
        return ElementFormAdmin


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Element, ElementAdmin)
