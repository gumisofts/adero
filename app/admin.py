from django.contrib import admin
from .models import *


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "detail"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "message", "service"]


class PositionAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Service, ServiceAdmin)
