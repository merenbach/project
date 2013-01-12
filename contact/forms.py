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
    cc_myself = forms.BooleanField(required=False, label='CC yourself?')

    # required_css_class = ''
    error_css_class = 'error'
    
    def __init__(self, *args, **kwargs):
       kwargs_new = {'error_class': InlineErrorList}
       if kwargs is not None:
           kwargs_new.update(kwargs)
       super(ContactForm, self).__init__(*args, **kwargs_new)

    def send_email(self, recipient_list):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['sender']
        cc_myself = self.cleaned_data['cc_myself']
        # Values of extra headers (i.e., reply-to) don't get sanitized. To help
        # prevent possible header injection attempts (via newline), pass along
        # the from_email as, well, the from email, which can raise an exception.
        from django.core.mail import EmailMessage
        email = EmailMessage(subject, message, from_email, recipient_list, headers={'Reply-To': from_email})
        email.send()
        if cc_myself:
            # Echo to sender separately to avoid divulging email addresses
            from django.core.mail import send_mail
            send_mail(subject, message, None, [from_email])

    # def akismet_check(self, request, message, sender, debug=False):
    #     """ Check a contact form submission with Akismet.  Return Yes for spam (or error), No for ham. """
    #     rv = True
    #     from akismet import Akismet
    #     api = Akismet(settings.AKISMET_API_KEY, settings.AKISMET_BLOG_URL)
    #     #agent='Django contact form'
    #     if api.verify_key():
    #         try:
    #             data = {
    #                 'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
    #                 'user_agent': request.META.get('USER_AGENT', ''),
    #                 'referrer': request.META.get('HTTP_REFERER', ''),
    #                 'comment_type': 'comment',
    #                 'comment_author': sender,
    #             }
    #             rv = api.comment_check(message.encode('utf-8'), data=data, build_data=True, DEBUG=debug)
    #         except:
    #             pass
    #     return rv

"""
    from akismet import Akismet

    api = Akismet(agent='Test Script')
    # if apikey.txt is in place,
    # the key will automatically be set
    # or you can call api.setAPIKey()
    #
    if api.key is None:
        print "No 'apikey.txt' file."
    elif not api.verify_key():
        print "The API key is invalid."
    else:
        # data should be a dictionary of values
        # They can all be filled in with defaults
        # from a CGI environment
        if api.comment_check(comment, data):
            print 'This comment is spam.'
        else:
            print 'This comment is ham.'
"""
