from django.urls import path

from . import views

app_name = 'blog'

urlpatterns=[
    path('',views.blog_home,name='homepage'),
    path('single/<int:id>',views.blog_single,name='singlehome'),
    path('test/<int:pid>',views.test,name='test'),
]