from django import template

register = template.Library()

from tony_blog.models import Post


@register.simple_tag
def total_posts_counts():
    c = 0
    for post in Post.published.all():
        if post.status == 'published':
            c += 1
    return c
