from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "app/index.html")


def about(request):
    return render(request, "app/about.html")


def career(request):
    return render(request, "app/career.html")


def faq(request):
    return render(request, "app/faq.html")


def test(request):
    return render(request, "app/test.html")
