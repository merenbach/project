from django.views.generic import TemplateView
from django.http import Http404
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
