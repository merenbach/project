from django.contrib.sitemaps import Sitemap
from software.models import Software

class SoftwareSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Software.objects.filter(is_published=True)

	def lastmod(self, obj):
		return obj.pub_date
