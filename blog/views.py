from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
current_time=timezone.now()


def blog_home(request,category_name=None,author_name=None):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    if category_name:
        posts=posts.filter(category__name=category_name)
    if author_name:
        posts=posts.filter(author__username=author_name)
    context={"post": posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,id):
    current_post=get_object_or_404(Post,id=id,status=1,published_date__lt=current_time)
    
    # all_post=Post.objects.filter(published_date__lt = current_time,status=1)
    try:
        next_post=Post.objects.filter(published_date__lt = current_time,status=1,id__gt=id).order_by('id').first()
    except:
        next_post=None

    try:
        perv_post=Post.objects.filter(published_date__lt = current_time,status=1,id__lt=id).order_by('-id').first()

    except:
        perv_post=None

    current_post.counted_views+=1
    current_post.save()
    context={'post':current_post,'next_post':next_post,'perv_post':perv_post}
    return render(request,'blog/blog-single.html', context)

def category_filter(request, category_name):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    posts=posts.filter(category__name=category_name)
    context={'post':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'post':posts}
    return render(request,'blog/blog-home.html',context)


def test(request):
    all_posts=Post.objects.all()
    context={'all_posts':all_posts}

    return render(request,'blog/test.html',context)
# Create your views here.
