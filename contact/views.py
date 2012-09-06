from django.conf import settings
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

def send_message(request):
    request.breadcrumbs('Contact', reverse('contact'))
    context_dict = {}
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
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
                    'X-Spam-Flag': 'Yes' if akismet_check(request, message, sender) else 'No',
                }
		from django.core.mail import send_mail
		email = EmailMessage(subject, message, sender, recipients, headers=headers)
		#send_mail(subject, message, sender, recipients)
		email.send()
		return HttpResponseRedirect('/contact/thanks/') # Redirect after POST
		#return HttpResponseRedirect(reverse('contact.views.send_message')) # Redirect after POST
            else:
		context_dict.update(form=form)
	    #return HttpResponseRedirect('/contact/') # Redirect after POST
        else:
            # validation failed
            context_dict.update(form=form)
    else:
        form = ContactForm() # An unbound form
        context_dict.update(form=form)
    return render_to_response('contact/contact.html', context_dict, context_instance=RequestContext(request))

def thanks(request):
    request.breadcrumbs(('Contact', reverse('contact')), ('Thanks', reverse('contact-thanks')))
    context_dict = {}
    #context_dict.update(thanks=True)
    return render_to_response('contact/thanks.html', context_dict, context_instance=RequestContext(request))

def akismet_check(request, message, sender, debug=False):
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
