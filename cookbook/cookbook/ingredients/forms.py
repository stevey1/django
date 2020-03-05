from graphene_django.forms.mutation import DjangoModelFormMutation
from django.db import models
from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'id')
