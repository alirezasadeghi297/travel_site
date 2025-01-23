from django.urls import path
from accounts import views

app_name = 'account'
urlpatterns=[
    # path('login_view',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    # path('sign_up',views.sign_up_view,name='sign_up'),
]