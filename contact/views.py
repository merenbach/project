from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from contact.forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-thanks')
    
    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs('Contact', reverse('contact'))
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']

            if settings.CONTACT_RECIPIENTS and len(settings.CONTACT_RECIPIENTS) > 0:
                recipients = settings.CONTACT_RECIPIENTS
                #if cc_myself:
                #    recipients.append(sender)
                headers = {
                    'Reply-To': sender,
                    'X-Spam-Flag': 'Yes' if self.akismet_check(self.request, message, sender) else 'No',
                }
                from django.core.mail import send_mail
                email = EmailMessage(subject, message, sender, recipients, headers=headers)
                #send_mail(subject, message, sender, recipients)
                email.send()
                # return HttpResponseRedirect(reverse('contact-thanks')) # Redirect after POST
        return super(ContactView, self).form_valid(form)

    def akismet_check(self, request, message, sender, debug=False):
        """ Check a contact form submission with Akismet.  Return Yes for spam (or error), No for ham. """
        rv = True
        from akismet import Akismet
        api = Akismet(settings.AKISMET_API_KEY, settings.AKISMET_BLOG_URL)
        #agent='Django contact form'
        if api.verify_key():
            try:
                data = {
                    'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                    'user_agent': request.META.get('USER_AGENT', ''),
                    'referrer': request.META.get('HTTP_REFERER', ''),
                    'comment_type': 'comment',
                    'comment_author': sender,
                }
                rv = api.comment_check(message.encode('utf-8'), data=data, build_data=True, DEBUG=debug)
            except:
                pass
        return rv

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'
    
    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([('Contact', reverse('contact')), ('Thanks', reverse('contact-thanks'))])
        return super(ContactThanksView, self).dispatch(request, *args, **kwargs)

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
