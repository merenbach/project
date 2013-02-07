from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe
from rsvp.models import Party
from django.template.loader import render_to_string

#class MyCheckboxSelectMultiple(CheckboxSelectMultiple):
#    def render(self, name, value, ulattrs=None, attrs=None, choices=()):
#        if value is None: value = []
#        has_id = attrs and 'id' in attrs
#        final_attrs = self.build_attrs(attrs, name=name)
#        output = [u'<ul class="%s">' % ulattrs.get('class')]
#        # Normalize to strings
#        str_values = set([force_unicode(v) for v in value])
#        for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
#            # If an ID attribute was given, add a numeric index as a suffix,
#            # so that the checkboxes don't all have the same ID attribute.
#            if has_id:
#                final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
#                label_for = u' for="%s"' % final_attrs['id']
#            else:
#                label_for = ''
#
#            cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
#            option_value = force_unicode(option_value)
#            rendered_cb = cb.render(name, option_value)
#            option_label = conditional_escape(force_unicode(option_label))
#            output.append(u'<li><label%s>%s %s</label></li>' % (label_for, rendered_cb, #option_label))
#        output.append(u'</ul>')
#        return mark_safe(u'\n'.join(output))

class ResponseCardForm(forms.Form):
    primary_invitees = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label='You')
    secondary_invitees = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label='Your entourage')
    message = forms.CharField(required=False, widget=forms.Textarea, label='An optional message')
    cc_myself = forms.BooleanField(required=False, label='Send yourself a confirmation?')
    
    def __init__(self, *args, **kwargs):
        self.primary_invitees = kwargs.pop('primary_invitees', None)
        self.secondary_invitees = kwargs.pop('secondary_invitees', None)
        super(ResponseCardForm, self).__init__(*args, **kwargs)
        self.members = self.primary_invitees
        if self.primary_invitees is not None:
            self.fields['primary_invitees'].choices = [(member.pk, member.name) for member in self.primary_invitees]
        if self.secondary_invitees is not None:
            self.fields['secondary_invitees'].choices = [(member.pk, member.name) for member in self.secondary_invitees]

    #def send_email(self, recipient_list):
    #    # send email using the self.cleaned_data dictionary
    #    subject = self.cleaned_data['subject']
    #    message = self.cleaned_data['message']
    #    from_email = self.cleaned_data['sender']
    #    cc_myself = self.cleaned_data['cc_myself']
    #    # Values of extra headers (i.e., reply-to) don't get sanitized. To help
    #    # prevent possible header injection attempts (via newline), pass along
    #    # the from_email as, well, the from email, which can raise an exception.
    #    from django.core.mail import EmailMessage
    #    email = EmailMessage(subject, message, from_email, recipient_list, headers={'Reply-To': #from_email})
    #    email.send()
    #    if cc_myself:
    #        # Echo to sender separately to avoid divulging email addresses
    #        from django.core.mail import send_mail
    #        send_mail(subject, message, None, [from_email])

    #def get_queryset(self):
    #    return self.get_model()
    
    def notify(self, party):
        """ Notify site managers about the RSVP """
        from django.core.mail import EmailMessage
        subject = 'Wedding RSVP notification'
        message = render_to_string('rsvp/notify.html', {'party': party})
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

    def confirm(self, invitation):
        """ Confirm RSVP with invitees """
        from django.core.mail import send_mail
        party = invitation.party
        if party.headcount > 0:
            rsvp_template_name = 'rsvp/confirm.html'
        else:
            rsvp_template_name = 'rsvp/confirm_no.html'
        message = render_to_string(rsvp_template_name, {
            'invitation': invitation,
            })
        send_mail('Wedding RSVP confirmation', message, None, party.emails())
