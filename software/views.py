from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from software.models import Software
from django.http import Http404

class SoftwareIndexView(ListView):
    template_name = 'software/index.html'
    context_object_name = 'software_list'
    queryset = Software.objects.filter(is_published=True).order_by('title')

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs('Software', reverse('software'))
        return super(SoftwareIndexView, self).dispatch(request, *args, **kwargs)

class SoftwareDetailView(DetailView):
    template_name = 'software/detail.html'
    queryset = Software.objects.filter(is_published=True).order_by('title')

    def dispatch(self, request, *args, **kwargs):
        # request.breadcrumbs(('Software', reverse('software')), (self.get_queryset().get_title(), reverse('software_detail')))
        return super(SoftwareDetailView, self).dispatch(request, *args, **kwargs)

class SoftwareTagView(ListView):
    template_name = 'software/software_list.html'
    context_object_name = 'software_list'
    allow_empty = True

    def dispatch(self, request, *args, **kwargs):
        # request.breadcrumbs('Software', reverse('software'))
        try:
            self.tag = kwargs.pop('tag')
        except KeyError:
            raise http404
        return super(SoftwareTagView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Software.objects.filter(is_published=True).order_by('title')
        # software = get_object_or_404(queryset, tags__=self.args[0])
        return queryset.filter(tags__contains=self.tag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SoftwareTagView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['tag'] = self.tag
        return context
