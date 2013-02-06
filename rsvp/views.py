from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from rsvp.models import Invitation, Party
from rsvp.forms import RespondezForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class InvitationView(TemplateView):
    template_name = 'rsvp/respondez.html'
    # form_class = RespondezForm
    # success_url = reverse_lazy('respondez-thanks')

    def dispatch(self, request, *args, **kwargs):
        try:
            self.party = Invitation.objects.get(slug__exact=kwargs.get('slug', None))
        except Invitation.DoesNotExist:
            raise Http404
        return super(InvitationView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InvitationView, self).get_context_data(**kwargs)
        context['party'] = self.party
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # attendee_ids = form.cleaned_data['attendees']
        #for person in self.party.members:
        #    if person.pk in attendee_ids:
        #        person.is_attending = True
        #    else:
        #        person.is_attending = False
        #form.confirm(self.party)
        #form.notify(self.party)
        return super(InvitationView, self).form_valid(form)


#class ResponseCardView(UpdateView):
#    model = ResponseCard

class ResponseCardThanksView(TemplateView):
    template_name = 'rsvp/thanks.html'
    
    def dispatch(self, request, *args, **kwargs):
        try:
            """ Verify that an entry for this site exists """
            self.party = Invitation.objects.get(slug__exact=kwargs.get('slug', None))
        except Invitation.DoesNotExist:
            raise Http404
        return super(ResponseCardThanksView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ResponseCardThanksView, self).get_context_data(**kwargs)
        context['party'] = self.party
        return context
