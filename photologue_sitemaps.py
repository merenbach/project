"""
To use, add the following to the sitemap definition section of your project's
urls.py:

...
from photologue.sitemaps import photologue_gallery, photologue_photo

sitemaps = {...
            'photologue_gallery': photologue_gallery,
            'photologue_photo': photologue_photo,
            ...
            }
etc...

Note: in photologue there can be multiple URLs that lead to the same objects
(same gallery, same photo) but we only include the 'canonical' one in the
sitemap to help Google decide on the best URL to index.
See also http://googlewebmastercentral.blogspot.com/2007/09/google-duplicate-content-caused-by-url.html

"""

from django.contrib.sitemaps import GenericSitemap
from photologue.models import Gallery, Photo

# For sitemap generation
gallery_args = {'date_field': 'date_added', 'queryset': Gallery.objects.filter(is_public=True)}
photo_args = {'date_field': 'date_added', 'queryset': Photo.objects.filter(is_public=True)}

photologue_gallery = GenericSitemap(gallery_args, priority=0.6)
photologue_photo = GenericSitemap(photo_args, priority=0.5)
