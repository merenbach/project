# README for Project

## Notes
- To get flatpages (per site) filtered per site search form *and* to get Software indexed and showing up on merenbach.com *only*, I had to rename the "site" attribute on the search index for Software to something like pub_site.  Maybe it was conflicting with something else, elsewhere in the system.

## TODO(NE)
Basically, we need(ed) to filter the sites being indexed.

This entails adjusting the SearchQuerySet, as described [here](http://stackoverflow.com/questions/6138604/how-to-django-haystack-multisite).

    from haystack.indexes import SearchIndex, IntegerField
    
    class SiteSearchIndex(SearchIndex):
        site_id = IntegerField(model_attr="site__id")

Then, in the URLConf:

    from django.conf import settings
    from django.conf.urls.defaults import patterns, url
    from haystack.forms import SearchForm
    from haystack.query import SearchQuerySet
    from haystack.views import search_view_factory
    from myapp.apps.search.views import SearchView
    
    sqs = SearchQuerySet().filter(site_id=settings.SITE_ID).order_by("-pub_date")
    urlpatterns = patterns("",
            url(r"^$",
                search_view_factory(
                    view_class=SearchView, searchqueryset=sqs, form_class=SearchForm
                    ),
                name="search-index"
               ),
            )

We need to find a way, however, to get the site id from the Site multivalued indexed attribute.  We may need to either find the ID from the site object(s) against which we are filtering, or otherwise (and perhaps a better option) find a Site object corresponding to the active Site ID.
