from django.shortcuts import render
from .models import *

import app.info as info
from django.utils import timezone
from .forms import ApplyJobForm
import json

services_list = [
    "Software Development",
    "IT Consultancy",
    "Education Consultancy",
    "Trainings and Courses",
    "Social Media Marketing",
    "Online Applications Processing",
]


class NavigationItem:
    def __init__(self, name, link) -> None:
        self.name = name
        self.link = link


nav_items = [
    NavigationItem("Home", "/"),
    NavigationItem("Services", "/services"),
    NavigationItem("About", "/about"),
    NavigationItem("Careers", "/careers"),
    NavigationItem("FAQ", "/faq"),
]

context = {
    "services_list": services_list,
    "services": info.services,
    "nav_items": nav_items,
}


def home(request):
    return render(
        request,
        "app/index.html",
        context={
            "nav_index": 1,
            **context,
        },
    )


def services(request):
    return render(
        request,
        "app/services.html",
        context={"nav_index": 2, **context},
    )


def about(request):
    services = Service.objects.all()
    return render(
        request,
        "app/about.html",
        context={
            "nav_index": 3,
            "services": info.services,
            "teams": User.objects.exclude(position=None),
            **context,
        },
    )


def career(request):
    return render(
        request,
        "app/career.html",
        context={
            "nav_index": 4,
            "open_positions": Position.objects.filter(is_open=True),
            **context,
        },
    )


def faq(request):
    return render(
        request,
        "app/faq.html",
        context={
            "nav_index": 5,
            "faqs": info.faqs,
            **context,
        },
    )


def contact_us(request):
    return render(
        request,
        "app/contact_us.html",
        context={"nav_index": 6, **context},
    )


def apply_job(request, id):

    if request.method == "POST":

        form = ApplyJobForm(request.POST, request.FILES)
        return render(
            request,
            "app/apply_job.html",
            context={
                "nav_index": 4,
                "position": Position.objects.get(id=id),
                "id": id,
                **context,
            },
        )

    return render(
        request,
        "app/apply_job.html",
        context={
            "nav_index": 4,
            "id": id,
            "form": ApplyJobForm(),
            "position": Position.objects.get(id=id),
            **context,
        },
    )


def softawre_service(request):
    return render(request, "app/softaware_services.html", context={**context})


def test(request):
    return render(request, "app/index2.html")


# Softaware Services
# Web apps
# Mobile applications
# Ecommerce
# Integrations: sms,payment
