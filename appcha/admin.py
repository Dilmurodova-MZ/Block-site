from django.contrib import admin
from .models import *

class name(admin.ModelAdmin):
    list_display = ['logo_img']
admin.site.register(Logo, name)

class name(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Home_page, name)
