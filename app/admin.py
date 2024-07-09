from django.contrib import admin
from .models import *


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "detail"]


admin.site.register(User)
admin.site.register(Service, ServiceAdmin)
