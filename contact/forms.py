from django import forms
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe 
from contact.decorators import decorate_bound_field
decorate_bound_field()


# decorate_bound_field()
# class LabelErrorList(ErrorList):
# def __unicode__(self):
#    return self.as_ul()

#def as_ul(self):
#    if not self: return u''
#    return u''.join([u'<li class="error label label-important">{}</li>'.format(e) for e in self])
#    #return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class InlineErrorList(ErrorList):
    def __unicode__(self):
        return self.as_ul()

    def as_ul(self):
        if not self: return u''
        errors_list = [u'<li>{}</li>'.format(e) for e in self]
        return mark_safe(u'<ul class="unstyled help-inline">{}</ul>'.format(''.join(errors_list)))

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
       kwargs_new = {'error_class': InlineErrorList}
       if kwargs is not None:
           kwargs_new.update(kwargs)
       super(ContactForm, self).__init__(*args, **kwargs_new)

    # required_css_class = ''
    error_css_class = 'error'
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-large'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-large'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-large'}))
    # cc_myself = forms.BooleanField(required=False)
    
    # For Bootstrap
    field_icons = {
        'subject': 'icon-tag',
        'message': 'icon-pencil',
        'sender': 'icon-envelope',
    }
