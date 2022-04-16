from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.views import generic
from employee.models import Employee
from service.models import Service
from questions.models import Question, Title
from project.models import Project
from .models import ColorSetting
# Create your views here.
class IndexView(generic.ListView):
    template_name="index/index.html"
    content_object_name="employee_list"

    def get_queryset(self):
        return Employee.objects.order_by("created")[:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_list"] = Service.objects.order_by("id")[:]
        context["question_list"] = Question.objects.order_by("-created")
        context["title_list"] = Title.objects.order_by("id")
        context["project_list"] = Project.objects.order_by("id")
        context["color"] = ColorSetting.objects.get(name="main color")
        context["menu_color"] = ColorSetting.objects.get(name="menu color")
        context["progress_bar_color"] = ColorSetting.objects.get(name="progress bar color")
        return context
    
def send_email(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    mail = request.POST.get('email', '')
    if subject and message and mail:
        message  += f" İsim: {name} Mail: {mail}"
        try:
            send_mail(subject, message, "berkayceylan150@gmail.com", ['worapsv@gmail.com'],fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.--')
        return HttpResponse('mail success--')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')