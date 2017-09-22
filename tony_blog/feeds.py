from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from tony_blog.models import Post


class LatestPostFeed(Feed):
    title = 'Tony blog'
    link = '/tony_blog/'
    description = "New Posts of Tony's blog"

    def items(self):
        return Post.objects.filter(status='published')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)