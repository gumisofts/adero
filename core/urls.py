from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("test/", test),
]
