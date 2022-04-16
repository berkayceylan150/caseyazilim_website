from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Title(models.Model):
    categ_name = models.CharField(max_length=100)
    main_title = models.BooleanField(default=False)

    def __str__(self):
        return self.categ_name
    

class Question(models.Model):
    question_name = models.CharField( max_length=200)
    question_body = HTMLField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.question_name
