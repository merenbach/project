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
        from django.core.mail import send_mail, mail_managers
        mail_managers(subject, message)

    def confirm_rsvp(self):
        from django.core.mail import send_mail
        message = render_to_string('rsvp/confirm.html',
            {
                'title': 'Maintenance Mode',
                'messages': messages
            }, context_instance=RequestContext(request))
        send_mail(subject, message, None, [settings])



