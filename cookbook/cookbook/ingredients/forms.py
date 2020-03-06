from django import forms
from django.core import validators
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'id')
        # error_message = {'name': {'max_length': _('This name is too long')}}

    def clean_name(self):
        data = self.cleaned_data['name']
        if "test" in data:
            raise forms.ValidationError(
                "This is not test mode", code='invalid')
        return data

    def clean(self):
        data = self.cleaned_data['name']
        if "test" in data:
            raise forms.ValidationError(
                "This is not test mode", code='invalid')
        return data
