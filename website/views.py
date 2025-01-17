from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def elements(request):
    return render(request,'website/elements.html')

def test2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()


    form=ContactForm()
    context={'form': form}
    return render(request,'website/test2.html',context)

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'good job')
        else:
            messages.add_message(request,messages.ERROR,'Invalid')
    form=ContactForm()
    context={'form': form}
    return render(request,'website/contact.html',context)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
# Create your views here.
