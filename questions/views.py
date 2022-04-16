from django.shortcuts import render
from django.views import generic
from .models import Question, Title, Setting
# Create your views here.
class IndexView(generic.ListView):
    template_name="questions/index.html" 
    content_object_name="question_list"
    
    def get_queryset(self):
        return Question.objects.order_by("-created")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_list"] = Title.objects.order_by("id")
        context["color"] = Setting.objects.filter(setting_name = "color")
        return context
    
    