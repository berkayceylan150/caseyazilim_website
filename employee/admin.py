from django.contrib import admin

from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeOptions(admin.ModelAdmin):
    list_display = ('name', 'title', 'brief', 'image_path', 'display_image',)
    # list_display = [field.name for field in Employee._meta.get_fields()] + ['display_image']
    list_display_links = ['name']
    list_editable = ( "title", "image_path")
class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)

class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)