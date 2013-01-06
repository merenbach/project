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
#    return u''.join([u'<li class="error label label-important">{0}</li>'.format(e) for e in self])
#    #return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class InlineErrorList(ErrorList):
    def __unicode__(self):
        return self.as_spans()

    def as_spans(self):
        if not self: return u''
        errors_list = [u'<small class="help-inline pull-right">{0}</small>'.format(e) for e in self]
        return mark_safe(u' '.join(errors_list))

    def as_ul(self):
        if not self: return u''
        errors_list = [u'<li>{0}</li>'.format(e) for e in self]
        return mark_safe(u'<ul class="unstyled help-inline">{0}</ul>'.format(''.join(errors_list)))

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False, label='Send me a copy')

    # required_css_class = ''
    error_css_class = 'error'
    
    def __init__(self, *args, **kwargs):
       kwargs_new = {'error_class': InlineErrorList}
       if kwargs is not None:
           kwargs_new.update(kwargs)
       super(ContactForm, self).__init__(*args, **kwargs_new)
