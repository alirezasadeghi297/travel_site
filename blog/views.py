from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
current_time=timezone.now()


def blog_home(request):
    post_pub=Post.objects.filter(published_date__lt = current_time,status=1)
    
    context={"post": post_pub}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,id):
    current_post=get_object_or_404(Post,id=id,status=1)
    
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


def test(request,pid):
    post=Post.objects.get(id=pid)
    context={'post':post}
    return render(request, 'blog/test.html',context)
# Create your views here.
