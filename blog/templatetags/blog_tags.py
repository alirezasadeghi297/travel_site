from django import template
from blog.models import Post,Comments
from blog.models import Category
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


@register.inclusion_tag('blog/blog_latest_post.html')
def latest_posts(args : int =2):
    posts=Post.objects.filter(status=1,published_date__lt=current_time).order_by('published_date')

    return {'latest_posts': posts[:args]}

@register.inclusion_tag('blog/blog_post_cat.html')
def categories():
    categories=Category.objects.all()
    posts=Post.objects.filter(status=1,published_date__lt=current_time)
    cat_names={}
    for name in categories:
        cat_names[name]=posts.filter(category=name).count()

    return {'categories': cat_names}

@register.inclusion_tag('blog/blog_home_tags.html')
def tags():
    tag_name = Post.objects.filter(status=1,published_date__lt=current_time).values_list('tags__name')
    tags=set()
    for tag in tag_name:
        
        tags.add(tag[0])
    tags.remove(None) 
    return {'tags': tags}


@register.inclusion_tag('website/website-blog_post.html')
def latest_blog_post():
    posts=Post.objects.filter(status=1,published_date__lt=current_time).order_by('published_date')[:6]
    
    return {'posts': posts}

@register.simple_tag(name='comments_counted')
def function(pid):
    return Comments.objects.filter(post=pid,approved=True).count()