from django.urls import path

from . import views

app_name = 'blog'

urlpatterns=[
    path('',views.blog_home,name='homepage'),
    path('single/<int:id>',views.blog_single,name='singlehome'),
    path('category/<str:category_name>',views.blog_home,name='category'),
    path('tags/<str:tag_name>',views.blog_home,name='tags'),
    path('author/<str:author_name>',views.blog_home,name='author'),
    path('test',views.test,name='test'),
    path('search',views.blog_search,name='search'),
]