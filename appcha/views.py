from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
  
def home(request):
    slayder = Home_page.objects.all()
    context = {
        'slayder':slayder,
    }
    return render(request, 'index.html', context)

def navbar_logo(request):
    logo_img = Logo.objects.all()
    context = {
        'logo_img':logo_img,
    }
    return render(request,'navbar.html',context)

def albums(request):
    album = Album.objects.all()
    context = {
        'album':album,
    }
    return render(request, 'albums.html', context)

def gallery(request):
    gall = Gallery.objects.all()
    context = {
        'gall':gall,
    }
    return render(request, 'gallery.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog,
    }
    return render(request, 'blog.html', context)

def Blog_pages(request, post_id):
    blog = get_object_or_404(Blog, pk=post_id)
    blog_title = Blog.objects.all()
    context = {
        'blog':blog,
        'blog_title':blog_title,
    }
    return render(request, 'blog-single-page.html', context)
    


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Send(request):
    user = UserForm(request.POST)
    if request.method == "POST":
        if user.is_valid():
            user.save()
            return redirect('home')
    else:
        user = UserForm()
    context = {
        'user':user
    }
    return render(request, 'contact.html', context)