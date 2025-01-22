from django.shortcuts import render

def login(request):
    return render(request,'account/login.html')

def sign_up(request):
    return render(request,'account/sign_up.html')
# Create your views here.
