from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('elements', views.elements,name='elements'),
    path('test',views.test2,name='test2'),
    path('contact',views.contact,name='contact'),
    path('newsletter',views.newsletter,name='newsletter'),
]