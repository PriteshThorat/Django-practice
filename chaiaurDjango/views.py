from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    #return HttpResponse("Hello from Home Page")
    return render(req, 'nav/home.html')

def about(req):
    #return HttpResponse("Hello from About Page")
    return render(req, 'nav/about.html')

def contact(req):
    #return HttpResponse("Hello from Contact Page")
    return render(req, 'nav/contact.html')