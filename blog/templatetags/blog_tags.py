from django import template
from blog.models import Post
from django.utils import timezone

current_time=timezone.now()
register = template.Library()

@register.simple_tag(name='total_posts')
def total():
    posts=Post.objects.filter(status=1,published_date__lt=current_time).count()
    return posts

@register.simple_tag(name='post_queri')

def posts():
    posts=Post.objects.filter(status=1,published_date__lt=current_time)
    return posts

@register.filter
def snippets(value,args : int =20):
    return value[:args]