import project.settings
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

def send_message(request):
    context_dict = {}
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']

            if settings.CONTACT_RECIPIENTS:
                recipients = settings.CONTACT_RECIPIENTS
                #if cc_myself:
                #    recipients.append(sender)

                from django.core.mail import send_mail
                email = EmailMessage(subject, message, sender, recipients, headers = {'Reply-To': sender})
                #send_mail(subject, message, sender, recipients)
                email.send()
                return HttpResponseRedirect('/contact/') # Redirect after POST
                #return HttpResponseRedirect(reverse('contact.views.send_message')) # Redirect after POST
            #return HttpResponseRedirect('/contact/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
        context_dict.update(form=form)
    return render_to_response('contact/contact.html', context_dict, context_instance=RequestContext(request))

#def thanks(request):
#    return render_to_response('contact/thanks.html')
