from django.shortcuts import render
from .models import *

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
    NavigationItem("About", "/about"),
    NavigationItem("Careers", "/careers"),
    NavigationItem("faq", "/faq"),
]


def home(request):
    return render(
        request,
        "app/index.html",
        context={
            "services_list": services_list,
            "nav_items": nav_items,
            "nav_index": 0,
        },
    )


def about(request):
    services = Service.objects.all()
    return render(
        request,
        "app/about.html",
        context={"services": services, "services_list": services_list, "nav_index": 2},
    )


def career(request):
    return render(
        request,
        "app/career.html",
        context={
            "services_list": services_list,
            "nav_index": 3,
        },
    )


def faq(request):
    return render(
        request,
        "app/faq.html",
        context={
            "services_list": services_list,
            "nav_index": 4,
        },
    )


def test(request):
    return render(request, "app/index2.html")
