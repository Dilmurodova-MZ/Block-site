from django.contrib import admin
from .models import *

class name(admin.ModelAdmin):
    list_display = ['logo_img']
admin.site.register(Logo, name)

class name(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Home_page, name)

class name(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(Category, name)

class name(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Album, name)

class name(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Blog, name)

class name(admin.ModelAdmin):
    list_display = ['img_url']
admin.site.register(Gallery, name)
