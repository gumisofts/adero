from django.shortcuts import render
from .models import *

import app.info as info
from django.utils import timezone
from .forms import *
import json

from django.template.loader import render_to_string

from core.mail import *
from core.recaptcha import *


class NavigationItem:
    def __init__(self, name, link) -> None:
        self.name = name
        self.link = link


nav_items = [
    NavigationItem("Home", "/"),
    NavigationItem("Services", "/services"),
    NavigationItem("About", "/about"),
    NavigationItem("Careers", "/careers"),
    NavigationItem("FAQs", "/faq"),
]
context = {
    "services_list": info.services_list,
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

    if request.method == "POST":

        recap = request.POST["g-recaptcha-response"]

        form = ContactForm(data=request.POST)

        if not form.is_valid() or not verify(recap):

            return render(
                request,
                "app/contact_us.html",
                context={"nav_index": 6, **context, "form": form},
            )

        send_email_html(
            subject=f"About {form.data['service']} Service",
            html_message=render_to_string(
                "email/service_request_customer.html",
                context={
                    "name": form.data["fullname"].strip().split()[0],
                    "service": form.data["service"],
                },
            ),
            to=form.data["email"],
        )
        send_email_managers(
            subject=f"About {form.data['service']} Service",
            html_message=render_to_string(
                "email/service_request_admin.html",
                context={
                    "mailto": f'mailto:{form.data["email"]}',
                    "message": form.data["message"],
                    "email": form.data["email"],
                    "fullname": form.data["fullname"],
                },
            ),
        )
        return render(
            request,
            "app/succesfull_contact_us.html",
            context={
                "nav_index": 6,
                **context,
                "message": "We Received your request. we will reachout to you as soon as possible",
                "continue_to": "/",
            },
        )
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


def education_consultancy(request):
    return render(request, "app/education_consultancy.html", context={**context})


def training_and_courses(request):
    return render(request, "app/training_and_courses.html", context={**context})


def test(request):
    return render(request, "app/index2.html")


# Softaware Services
# Web apps
# Mobile applications
# Ecommerce
# Integrations: sms,payment
