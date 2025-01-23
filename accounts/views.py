from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import sign_up_form
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user= authenticate(request, username=username , password=password)
            if user is not None:
                login(request, user)    
                return redirect('/')
            else:
                print('user not found')
    else:
        return redirect('/')
    return render(request,'account/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def sign_up_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = sign_up_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print('not valid')


        form=sign_up_form()
        context={'form': form}
        return render(request,'account/sign_up.html',context)
    else:
        return redirect('/')
    
# Create your views here.
