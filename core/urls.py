from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path("", home),
    path("about/", about),
    path("careers/", career),
    path("faq/", faq),
    path("admin/", admin.site.urls),
    path("test/", test),
]
