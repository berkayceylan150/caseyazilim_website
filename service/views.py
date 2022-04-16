from django.shortcuts import render
from django.views import generic
from .models import ServiceElement, Service
from project.models import Project
# Create your views here.
class ServiceView(generic.ListView):
    template_name = "service/service.html"
    model = ServiceElement
    
    def get_queryset(self):
        return ServiceElement.objects.filter(service=self.kwargs['pk']).order_by("id")[:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_list"] = Project.objects.filter(service=self.kwargs['pk']).order_by("created")[:]
        return context
   
    
