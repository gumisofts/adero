from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "app/index.html")


def about(request):
    services = Service.objects.all()
    return render(request, "app/about.html", context={"services": services})


def career(request):
    return render(request, "app/career.html")


def faq(request):
    return render(request, "app/faq.html")


def test(request):
    return render(request, "app/index2.html")
