from django import forms
from django.template.loader import render_to_string

class ResponseCardForm(forms.Form):
    primary_invitees = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label='You')
    secondary_invitees = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label='Your entourage')
    message = forms.CharField(required=False, widget=forms.Textarea, label='An optional message')
    cc_myself = forms.BooleanField(required=False, label='Send yourself a confirmation?')
    
    def __init__(self, *args, **kwargs):
        self.primary_invitees = kwargs.pop('primary_invitees', None)
        self.secondary_invitees = kwargs.pop('secondary_invitees', None)
        super(ResponseCardForm, self).__init__(*args, **kwargs)
        if self.primary_invitees is not None:
            self.fields['primary_invitees'].choices = [(member.pk, member.name) for member in self.primary_invitees]
            if self.secondary_invitees is not None:
                self.fields['secondary_invitees'].choices = [(member.pk, member.name) for member in self.secondary_invitees]
    
    def notify(self, invitation):
        """ Notify site managers about the RSVP """
        # from django.core.mail import EmailMessage
        from django.core.mail import mail_managers
        subject = 'Wedding RSVP notification'
        message = render_to_string('rsvp/notify.html', {'invitation': invitation})
        mail_managers(subject, message)
        # email = EmailMessage(subject, message, from_email, recipient_list)
        # email.send()

    def confirm(self, invitation, domain):
        """ Confirm RSVP with invitees """
        from django.core.mail import send_mail
        party = invitation.party
        if party.headcount > 0:
            rsvp_template_name = 'rsvp/confirm.html'
        else:
            rsvp_template_name = 'rsvp/confirm_no.html'
        message = render_to_string(rsvp_template_name, {
            'invitation': invitation,
            'domain': domain,
            })
        send_mail('Wedding RSVP confirmation', message, 'rsvp@theromantics.net', party.emails())
