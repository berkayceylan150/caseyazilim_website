from django.urls import path

from . import views
app_name="project"

urlpatterns = [
    path('<int:pk>', views.ProjectView.as_view(), name="project"),
]