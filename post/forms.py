from templates.back import *
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class PostingForms(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('judul', 'body', 'category')
        widget = {
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'aria-label': 'Username',
                    'aria-describedby':'basic-addon1',
                }
            ),
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '20',
                    'cols': '10',
                    'required': True,
                }
            ),
            "category" : forms.Select(
                attrs={
                    'class': 'dropdown-item',
                    'id': 'choices-button',
                    'required': True,
                    'name':'choices-button',
                    'placeholder': 'Departure',
                }
            ),
        }