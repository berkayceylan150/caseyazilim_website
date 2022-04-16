from email.policy import default
import re
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import Group

from tinymce.models import HTMLField
from colorfield.fields import ColorField
# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=255,)
    slug = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    detail = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # self.slug = re.sub("\W+" , "", self.slug.lower())
        # self.slug = re.sub(ur'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', u'', self.slug.lower())
        # self.slug = re.sub(r'[^\x00-\x7f]', r'-', self.slug.lower())
        tr2eng = self.slug.maketrans("çğıöşü", "cgiosu")
        self.slug = str(self.slug.lower().translate(tr2eng))
        self.slug = re.sub("\W+" ,r"-", self.slug.strip())

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=255,)
    slug = models.CharField(max_length=255, unique=True)
    detail = models.TextField()

    def save(self, *args, **kwargs):
        tr2eng = self.slug.maketrans("çğıöşü", "cgiosu")
        self.slug = str(self.slug.lower().translate(tr2eng))
        self.slug = re.sub("\W+" ,r"-", self.slug.strip())

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    visibility = models.ForeignKey(Group, blank=True, null = True, on_delete=models.CASCADE)
    color_text = ColorField(default='#000000')
    color_bg = ColorField(default='#FFFFFF')
    on_footer = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    uppercase = models.BooleanField(default=False)
    html_anchor = models.CharField(max_length=255, blank=True)
    extra_css_classes = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(Category, blank=True, default=[0])
    tags = models.ManyToManyField(Tag, blank=True, default=[0])
    def __str__(self):
        return self.title