from django.contrib.sitemaps import Sitemap
from tony_blog.models import Post


class PostSiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish
