from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employee.models import Employee
from project.models import Project
import json
# Create your views here.
def getInfo(type, operation):
    if(type == "employee"):
        if(operation == "getAll"):
            return list(Employee.objects.values())
    if(type == "project"):
        if(operation == "getAll"):
            return list(Project.objects.values())
@csrf_exempt
def index(request):
    if request.method == 'POST':
        type = request.POST["type"]
        operation = request.POST["operation"]
        return JsonResponse(getInfo(type, operation), safe=False)
    else:
        return JsonResponse(getInfo("employee", "getAll"), safe=False)
