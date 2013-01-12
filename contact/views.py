from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from contact.forms import ContactForm
from contact.models import ContactPage

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-thanks')
    
    def dispatch(self, request, *args, **kwargs):
        try:
            """ Verify that an entry for this site exists """
            self.contact_page = ContactPage.objects.get(site__id__exact=get_current_site(request).id)
            self.recipients = [str(r) for r in self.contact_page.recipients.all()]
        except ContactPage.DoesNotExist:
            raise Http404
        request.breadcrumbs('Contact', reverse('contact'))
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(self.recipients)
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact_page'] = self.contact_page
        return context

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'
    
    def dispatch(self, request, *args, **kwargs):
        try:
            """ Verify that an entry for this site exists """
            self.contact_page = ContactPage.objects.get(site__id__exact=get_current_site(request).id)
        except ContactPage.DoesNotExist:
            raise Http404
        request.breadcrumbs([('Contact', reverse('contact')), ('Thanks', reverse('contact-thanks'))])
        return super(ContactThanksView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ContactThanksView, self).get_context_data(**kwargs)
        context['contact_page'] = self.contact_page
        return context
