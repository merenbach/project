from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from rsvp.forms import ResponseCardForm
from rsvp.models import Invitation

class CookieView(View):
    def dispatch(self, request, *args, **kwargs):
        # super(CookieView, self).dispatch(request, *args, **kwargs)
        token = request.session.get('token')
        if token:
            return HttpResponseRedirect(reverse('rsvp-envelope', kwargs={'slug': token}))
        else:
            raise Http404

class EnvelopeView(TemplateView):
    template_name = 'rsvp/envelope.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.invitation = Invitation.objects.get(slug__exact=kwargs.get('slug'))
            request.session.update({'token': self.invitation.slug})
            # if self.invitation.is_viewed:
            #     from django.shortcuts import redirect
            #     from django.core.urlresolvers import reverse
            #     return redirect(reverse('rsvp-invitation', kwargs=kwargs), permanent=False)
        except Invitation.DoesNotExist:
            raise Http404
        return super(EnvelopeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EnvelopeView, self).get_context_data(**kwargs)
        context['token'] = self.invitation.slug
        context['formal_name'] = self.invitation.formal_name
        return context

class InvitationView(TemplateView):
    template_name = 'rsvp/invitation.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.invitation = Invitation.objects.get(slug__exact=kwargs.get('slug'))
            request.session.update({'token': self.invitation.slug})
            if not self.invitation.is_viewed:
                self.invitation.is_viewed = True
                self.invitation.save()
        except Invitation.DoesNotExist:
            raise Http404
        return super(InvitationView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InvitationView, self).get_context_data(**kwargs)
        context['slug'] = self.invitation.slug
        context['party'] = self.invitation.party
        return context

class ResponseCardView(FormView):
    template_name = 'rsvp/response_card.html'
    form_class = ResponseCardForm
    success_url = reverse_lazy('rsvp-response-thanks')

    def get_form_kwargs(self):
        k = super(ResponseCardView, self).get_form_kwargs()
        extra_dict = {
            "primary_invitees": self.invitation.party.members.filter(is_party_leader=True),
            "secondary_invitees": self.invitation.party.members.filter(is_party_leader=False),
        }
        k.update(extra_dict)
        return k

    def dispatch(self, request, *args, **kwargs):
        try:
            self.invitation = Invitation.objects.get(slug__exact=kwargs.get('slug'))
            request.session.update({'token': self.invitation.slug})
        except Invitation.DoesNotExist:
            raise Http404
        return super(ResponseCardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ResponseCardView, self).get_context_data(**kwargs)
        party = self.invitation.party
        context['slug'] = self.invitation.slug
        context['party'] = party
        context['leaders'] = party.members.filter(is_party_leader=True)
        context['followers'] = party.members.filter(is_party_leader=False)
        context['missing'] = party.size - party.headcount
        return context

    def form_valid(self, form):
        members = self.invitation.party.members.all()
        # attending_pks = []

        # Get the pks of the attendees
        primary_attendees = [int(i) for i in form.cleaned_data.get('primary_invitees', [])]
        secondary_attendees = [int(i) for i in form.cleaned_data.get('secondary_invitees', [])]

        for m in members:
            m.is_attending = False
            # Don't save yet

        primary_members = [m for m in members if m.pk in primary_attendees]
        secondary_members = [m for m in members if m.pk in secondary_attendees]

        for m in primary_members:
            m.is_attending = True

        if len(primary_members) > 0:
            for m in secondary_members:
                m.is_attending = True

        for m in members:
            m.save()

        message = form.cleaned_data.get('message')
        if message:
            self.invitation.response_message = message
            self.invitation.save()

        if form.cleaned_data.get('cc_myself', False):
            from rsvp.utils import get_full_domain
            form.confirm(self.invitation, get_full_domain(self.request))

        form.notify(self.invitation)

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
        return super(ResponseCardView, self).form_valid(form)

class ResponseCardThanksView(TemplateView):
    template_name = 'rsvp/thanks.html'
    
    def dispatch(self, request, *args, **kwargs):
        token = request.session.get('token')
        if token:
            return super(ResponseCardThanksView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

    #def get_context_data(self, **kwargs):
    #    context = super(ResponseCardThanksView, self).get_context_data(**kwargs)
    #    context['party'] = self.party
    #    return context
