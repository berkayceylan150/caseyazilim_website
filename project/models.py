from django import forms
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from tinymce.models import HTMLField
from service.models import Service
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="project_images", default="")
    def __str__(self) -> str:
        return str(self.image)
    def display_image(self):
        return format_html('<img src="%s" width="100px">' % self.image.url)
    display_image.allow_tags = True    

class Project(models.Model):
    name = models.CharField(max_length=150)
    not_software_project = models.BooleanField(default=False)
    main_image = models.ForeignKey(Image, related_name= "project_main_image", on_delete=models.CASCADE, default=[0], blank=True)
    images = models.ManyToManyField(Image, blank=True, default=[0])
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    language_technologies = models.TextField(blank=True)
    short_detail = models.CharField(max_length=150, blank=True)
    detail = HTMLField(blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
    def image(self):
        return format_html('<img src="%s" width="300px">' % self.main_image.image.url)
    image.allow_tags = True