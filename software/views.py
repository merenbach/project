#from django.template import Context, loader

#from django.shortcuts import render_to_response, get_object_or_404
#from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
#from django.template import RequestContext
#from software.models import Software
#
#from tagging.models import Tag, TaggedItem
#import models
#
#def tags(request):
#    return shortcuts.render_to_response('software/tags.html')
#
#def with_tag(request, tag, object_id=None, page=1):
#    query_tag = Tag.objects.get(name=tag)
#    software = TaggedItem.objects.get_by_model(models.Software, query_tag)
#    software = software.order_by('-pub_date')
#    return render_to_response('software/with_tag.html', dict(tag=tag, software=software))

#from django.http import HttpResponse

#def index(request):
#	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#	return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
#
##def index(request):
##	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
##	t = loader.get_template('polls/index.html')
##	c = Context({
##		'latest_poll_list': latest_poll_list,
##		})
##	return HttpResponse(t.render(c))
##	#output = ', '.join([p.question for p in latest_poll_list])
##	#return HttpResponse(output)
##	#return HttpResponse("Hello, world.  You're at the very cool poll index.")
#
#def detail(request, poll_id):
#	p = get_object_or_404(Poll, pk=poll_id)
#	return render_to_response('polls/detail.html', {'poll': p},
#			context_instance=RequestContext(request))
#	#try:
#	#	p = Poll.objects.get(pk=poll_id)
#	#except Poll.DoesNotExist:
#	#	raise Http404
#	#return render_to_response('polls/detail.html', {'poll': p})
#	#return HttpResponse("You're looking at the (very cool) poll %s." % poll_id)
#
#def results(request, poll_id):
#	p = get_object_or_404(Poll, pk=poll_id)
#	return render_to_response('polls/results.html', {'poll': p})
##return HttpResponse("You're looking at the (even cooler) results of the (very cool) poll %s." % poll_id)

#def vote(request, poll_id):
#	p = get_object_or_404(Poll, pk=poll_id)
#	try:
#		selected_choice = p.choice_set.get(pk=request.POST['choice'])
#	except (KeyError, Choice.DoesNotExist):
#		# Redisplay the poll voting form.
#		return render_to_response('polls/detail.html', {
#			'poll': p,
#			'error_message': "You didn't select a (very cool) choice.",
#			}, context_instance=RequestContext(request))
#	else:
#		selected_choice.votes += 1
#		selected_choice.save()
#		return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
#		#return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
#	
#	return HttpResponse("You're voting on (the very-soon-to-be-very-cool) poll %s." % poll_id)
#

# Create your views here.

#def detail(request, slug):
#	s = get_object_or_404(Software, pk=slug)
#	#request.breadcrumbs(_("About"), request.path_info)
#	return render_to_response('software/detail.html', {'software': s })
##	p = get_object_or_404(Poll, pk=poll_id)
##	return render_to_response('polls/results.html', {'poll': p})
