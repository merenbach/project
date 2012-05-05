from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from articles.models import Article

class ArticleSitemap(Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Article.objects.live().filter(is_active=True).all()

	def lastmod(self, obj):
		return obj.publish_date

	#def location(self, obj):
	#	return obj

