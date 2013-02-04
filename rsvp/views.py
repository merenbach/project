from django.views.generic import TemplateView
from django.http import Http404
from django.template.loader import render_to_string
from rsvp.models import Party

class RespondezView(TemplateView):
    template_name = 'rsvp/respondez.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.party = Party.objects.get(token__exact=kwargs.get('token', None))
        except Party.DoesNotExist:
            raise Http404
        return super(RespondezView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RespondezView, self).get_context_data(**kwargs)
        context['party'] = self.party
        return context

    def rsvp(self):
        # send email using the self.cleaned_data dictionary
        party = None
        subject = '{0} has just RSVPed for your wedding'.format(party.name)
        message = '{0} included the following message: {1}'.format(party.name, party.message)
        # Echo to sender separately to avoid divulging email addresses

    def confirm_rsvp(self, party):
        from django.core.mail import mail_managers
        message = render_to_string('rsvp/notify.html', {'party': party})
        mail_managers("Wedding RSVP notification", message)

    def confirm_rsvp(self, party):
        from django.core.mail import send_mail
        if party.is_attending:
            rsvp_template_name = 'rsvp/confirm.html'
        else:
            rsvp_template_name = 'rsvp/confirm_no.html'
        message = render_to_string(rsvp_template_name, {'party': party})
        send_mail('Wedding RSVP confirmation', message, None, [invitee.email for invitee in party.members if invitee.email])
