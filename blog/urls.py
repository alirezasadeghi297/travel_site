from django.urls import path

from . import views

app_name = 'blog'

urlpatterns=[
    path('',views.blog_home,name='homepage'),
    path('single',views.blog_single,name='singlehome'),
]