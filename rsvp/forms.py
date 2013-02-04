from django.forms import ModelForm, CheckboxSelectMultiple
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe
from rsvp.models import Party

class RespondezForm(ModelForm):
    class Meta:
        model = Party
        fields = ('members',)
        widgets = {
            'members': CheckboxSelectMultiple(),
        }
    
    def notify(self, party):
        """ Notify site managers about the RSVP """
        from django.core.mail import mail_managers
        message = render_to_string('rsvp/notify.html', {'party': party})
        mail_managers("Wedding RSVP notification", message)

    def confirm(self, party):
        """ Confirm RSVP with invitees """
        from django.core.mail import send_mail
        if party.is_attending:
            rsvp_template_name = 'rsvp/confirm.html'
        else:
            rsvp_template_name = 'rsvp/confirm_no.html'
        message = render_to_string(rsvp_template_name, {'party': party})
        send_mail('Wedding RSVP confirmation', message, None, [invitee.email for invitee in party.members if invitee.email])
