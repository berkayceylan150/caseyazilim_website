from django.contrib import admin
from .models import Service, ServiceElement, ServiceSetting, Image
# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceElement)
admin.site.register(ServiceSetting)
admin.site.register(Image)