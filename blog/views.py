from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_home(request):

    # posts=Post.objects.filter(status=1)
    current_time = timezone.now()
    post_pub=Post.objects.filter(published_date__lt = current_time,status=1)
    
    
    context={"post": post_pub}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,id):
    post=get_object_or_404(Post,id=id,status=1)
    # post=Post.objects.get(id=id)
    post.counted_views+=1
    post.save()
    context={'post':post}
    return render(request,'blog/blog-single.html', context)

def test(request,pid):
    post=Post.objects.get(id=pid)
    context={'post':post}
    return render(request, 'blog/test.html',context)
# Create your views here.
