from django.forms import Form
from django import forms


class ApplyJobForm(Form):
    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "border-black rounded-0"}),
    )
    email = forms.EmailField(label="Email")
    resume = forms.FileField(
        label="Resume",
        widget=forms.FileInput(
            attrs={
                "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
            },
        ),
    )
