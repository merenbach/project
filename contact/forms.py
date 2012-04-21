from django.db import models

# Create your models here.

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-block-level'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    #cc_myself = forms.BooleanField(required=False)
