from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

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