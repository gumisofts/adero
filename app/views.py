from django.shortcuts import render
from .models import *

import app.info as info

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


def home(request):
    return render(
        request,
        "app/index.html",
        context={
            "services_list": services_list,
            "nav_items": nav_items,
            "nav_index": 1,
            "services": info.services,
        },
    )


def services(request):
    return render(
        request,
        "app/services.html",
        context={
            "services_list": services_list,
            "nav_items": nav_items,
            "services": info.services,
            "nav_index": 2,
        },
    )


def about(request):
    services = Service.objects.all()
    return render(
        request,
        "app/about.html",
        context={
            "services": services,
            "services_list": services_list,
            "nav_index": 3,
            "nav_items": nav_items,
            "services": info.services,
        },
    )


def career(request):
    return render(
        request,
        "app/career.html",
        context={
            "services_list": services_list,
            "nav_index": 4,
            "nav_items": nav_items,
        },
    )


def faq(request):
    return render(
        request,
        "app/faq.html",
        context={
            "services_list": services_list,
            "nav_index": 5,
            "nav_items": nav_items,
            "faqs": info.faqs,
        },
    )


def contact_us(request):
    return render(
        request,
        "app/contact_us.html",
        context={
            "services_list": services_list,
            "nav_index": 6,
            "nav_items": nav_items,
        },
    )


def test(request):
    return render(request, "app/index2.html")
