from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from project.websites.merenbach.software.models import Software

class SoftwareSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Software.objects.all()

	def lastmod(self, obj):
		return obj.pub_date

	#def location(self, obj):
	#	return obj
