from pathlib import Path
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv(override=True)

env = os.environ.get

BASE_DIR = Path(__file__).resolve().parent.parent

LOCAL_DEV = env("LOCAL_DEV")

SECRET_KEY = env("SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "adero.gumiapps.com",
    "adero.tech",
    "www.adero.tech",
    "192.168.0.109",
    ".vercel.app",
]

AUTH_USER_MODEL = "app.User"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# COMPRESS_ROOT = env("STATIC_ROOT", "static")

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    "compressor.finders.CompressorFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
# Replace the DATABASES section of your settings.py with this
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": tmpPostgres.path.replace("/", ""),
        "USER": tmpPostgres.username,
        "PASSWORD": tmpPostgres.password,
        "HOST": tmpPostgres.hostname,
        "PORT": 5432,
        "OPTIONS": dict(parse_qsl(tmpPostgres.query)),
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]
STATIC_URL = env("STATIC_URL")
STATIC_ROOT = env("STATIC_ROOT")

MEDIA_ROOT = env("MEDIA_ROOT", "medias")

MEDIA_URL = env("MEDIA_URL", "medias/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_USE_SSL = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")

ADMINS = (("Nurad", "nuradhussen082@gmail.com"),)
MANAGERS = (("Yayha", "contact@adero.tech"),)

RE_CAPTCHA_SITE_KEY = env("RE_CAPTCHA_SITE_KEY")
RE_CAPTCHA_SECRET = env("RE_CAPTCHA_SECRET")
RE_CAPTCHA_PROJECT_ID = env("RE_CAPTCHA_PROJECT_ID")
GCLOUD_API_KEY = env("GCLOUD_API_KEY")
