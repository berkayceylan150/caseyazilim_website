from django.db import models
from colorfield.fields import ColorField
from optimized_image.fields import OptimizedImageField
# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=100, unique=True)
    service_detail = models.TextField()
    service_color = ColorField()
    bg_image = models.ImageField()

    def __str__(self):
        return self.service_name

class Image(models.Model):
    image = models.ImageField(upload_to="service_images/")
    def __str__(self):
        return str(self.image)
    
class ServiceElement(models.Model):
    element_title = models.CharField(max_length=300)
    image_field = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True)
    element_detail = models.TextField()
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.element_title

class ServiceSetting(models.Model):
    setting_name = models.CharField(max_length=100)
    setting_value = models.CharField(max_length=100)