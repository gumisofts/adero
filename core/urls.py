from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path("", home),
    path("about/", about),
    path("services/", services),
    path("careers/", career),
    path("faq/", faq),
    path("contact_us/", contact_us),
    path("apply_job/<int:id>", apply_job),
    path("admin/", admin.site.urls),
    path("test/", test),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
