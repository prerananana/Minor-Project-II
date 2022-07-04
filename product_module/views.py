from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html',{})
def about(request):
    return render(request, 'about.html', {})
def packages(request):
    return render(request, 'packages.html', {})
def destination(request):
    return render(request, 'travel_destination.html', {})
def blog(request):
    return render(request, 'blog.html', {})
def singleblog(request):
    return render(request, 'single-blog.html', {})
def contact(request):
    return render(request, 'contact.html', {})
def destination_details(request):
    return render(request, 'destination_details.html', {})
def elements(request):
    return render(request, 'elements.html', {})
def login(request):
    return render(request, 'login.html', {})
def registration(request):
    return render(request, 'registration.html', {})
