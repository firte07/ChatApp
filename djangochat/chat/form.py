from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['value', 'date', 'user', 'room', 'header_image']


class ImageForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
