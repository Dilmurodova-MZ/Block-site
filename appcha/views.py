from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'index.html')

def navbar_logo(request):
    logo_img = Logo.objects.all()
    context = {
        'logo_img':logo_img,
    }
    return render(request,'navbar.html',context)

def albums(request):
    return render(request, 'albums.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')