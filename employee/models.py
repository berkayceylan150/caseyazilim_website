from django.utils import timezone
from django.db import models
from django.utils.html import format_html

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    brief = models.TextField()
    image_path = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    def display_image(self):
        return format_html('<img width="100px" src="%s"/>' % self.image_path.url)
    display_image.allow_tags = True