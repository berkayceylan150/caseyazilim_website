from django.contrib import admin
from django.db import models
from .models import Project, Image
# Register your models here.

@admin.register(Project)
class ProjectOptions(admin.ModelAdmin):
    # list_display = ('name', 'title', 'brief', 'image_path', 'created',)
    list_display = ('id', 'name', 'service', 'short_detail', 'image')
    list_display_links = ('id', 'name', 'image')
    list_editable = ('service', 'short_detail')
    

@admin.register(Image)
class ImageOptions(admin.ModelAdmin):
    # list_display = ('name', 'title', 'brief', 'image_path', 'created',)
    list_display = ['display_image']
    list_display_links = ['display_image']
    