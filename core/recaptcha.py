from django.conf import settings
from django.core.cache import cache
import requests


def create_assessment(token):
    data = {
        "event": {
            "token": token,
            "expectedAction": "CONTACT",
            "siteKey": settings.RE_CAPTCHA_SITE_KEY,
        }
    }

    res = requests.post(
        f"https://recaptchaenterprise.googleapis.com/v1/projects/gumiapps/assessments?key={settings.GCLOUD_API_KEY}",
        json=data,
    )

    return res


def verify(token):
    res = create_assessment(token)
    print(res.json())

    if cache.get(token):
        return True

    return res.status_code == 200 and res.json()["tokenProperties"]["valid"]
