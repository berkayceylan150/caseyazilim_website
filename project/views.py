from django.shortcuts import render
from django.views import generic
from .models import Project
# Create your views here.

class ProjectView(generic.DeleteView):
    template_name = "project/project.html"
    model = Project