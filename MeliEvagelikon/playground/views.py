from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return HttpResponse("Welcome to the home page!")

def say_hello(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')


