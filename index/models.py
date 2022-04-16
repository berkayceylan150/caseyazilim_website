from django.db import models
from colorfield.fields import ColorField
# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class ColorSetting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = ColorField()

    def __str__(self):
        return self.name
    