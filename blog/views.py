from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comments
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommnetsForm
from django.contrib import messages

current_time=timezone.now()


def blog_home(request,category_name=None,author_name=None,tag_name=None):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    if category_name:
        posts=posts.filter(category__name=category_name)
    if author_name:
        posts=posts.filter(author__username=author_name)
    if tag_name:
        posts=posts.filter(tags__name__in=[tag_name])
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    try:
        posts= paginator.get_page(page_number)
    except PageNotAnInteger:
        posts=paginator.get_page(1)
    except EmptyPage:
        posts=paginator.get_page(paginator.num_pages)
    
    context={"post": posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,id):
    if request.method=='POST':
        form=CommnetsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited')
        else:
            messages.add_message(request,messages.ERROR,'something went wrong')

    # form=CommentsForm()
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
    comments=Comments.objects.filter(post=current_post,approved=True).order_by('-created_date')
    context={'post':current_post,'next_post':next_post,'perv_post':perv_post,'comments':comments}
    return render(request,'blog/blog-single.html', context)

def category_filter(request, category_name):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    posts=posts.filter(category__name=category_name)
    context={'post':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts=Post.objects.filter(published_date__lt = current_time,status=1)
    if request.method == 'GET':
        s=request.GET.get('s')
        posts=posts.filter(content__contains=s)
    context={'post':posts}
    return render(request,'blog/blog-home.html',context)


def test(request):
    all_posts=Post.objects.all()
    context={'all_posts':all_posts}

    return render(request,'blog/test.html',context)
# Create your views here.
