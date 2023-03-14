from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('albums/', albums, name='albums'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/<uuid:post_id>/', Blog_pages, name="blog"),
]