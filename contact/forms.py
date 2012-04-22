from django.db import models

# Create your models here.

from django import forms
from django.forms.util import ErrorList

class LabelErrorList(ErrorList):
    def __unicode__(self):
        return self.as_ul()

    def as_ul(self):
        if not self: return u''
        return u'<ul class="errorlist unstyled clearfix">{}</ul>'.format(''.join([u'<li class="error label label-important">{}</li>'.format(e) for e in self]))
        #return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': LabelErrorList}
        kwargs_new.update(kwargs)
        super(ContactForm, self).__init__(*args, **kwargs_new)

    #error_class = LabelErrorList
    error_css_class = 'error'
    required_css_class = 'control-group clearfix'
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-block-level'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    #cc_myself = forms.BooleanField(required=False)
