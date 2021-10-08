"""Django settings for {{cookiecutter.git_project_name}} project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', '!!!SET DJANGO_SECRET_KEY!!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {% if cookiecutter.DEBUG == 'True' %}True{% else %}False{% endif %}

ALLOWED_HOSTS = ["{{cookiecutter.ALLOWED_HOSTS}}"]

INTERNAL_IPS = ["{{cookiecutter.INTERNAL_IPS}}"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
{% if cookiecutter.use_django_allauth == "y" %}
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
{% endif %}
]
{% if cookiecutter.SITE_ID == "1" %}
SITE_ID = 1
{% else %}
SITE_ID = {{cookiecutter.SITE_ID}}
{% endif %}
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ cookiecutter.project_slug}}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                {% if cookiecutter.use_django_allauth == "y" %}
                "django.template.context_processors.request",
                {% endif %}
            ],
        },
    },
]
{% if cookiecutter.use_django_allauth == "y" %}
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
{% endif %}
WSGI_APPLICATION = "{{ cookiecutter.project_slug}}.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
{%- set language_labels = ({
    "en": "English",
    "cn": "Chinese",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "it": "Italian",
    "jp": "Japanese",
    "ru": "Russian",
    "es": "Spanish",
}) %}
{% if cookiecutter.USE_I18N == "True" %}
{% if cookiecutter.USE_L10N == "True" %}
USE_L10N = True
{% else %}
USE_L10N = False
{% endif %}
USE_I18N = True

LANGUAGE_CODE = "{{cookiecutter.LANGUAGE_CODE}}"

{%- with languages = cookiecutter.LANGUAGES.replace(' ', '').split(',') %}

LANGUAGES = [{% for language in languages %}
    ('{{ language }}', _("{{ language_labels[language] }}")),{% endfor %}
]
{% endwith %}

USE_TZ = True

TIME_ZONE = "{{cookiecutter.TIME_ZONE}}"
{% else %}
{% if cookiecutter.USE_L10N == "True" %}
USE_L10N = True
{% else %}
USE_L10N = False
{% endif %}
USE_I18N = False

LANGUAGE_CODE = "{{cookiecutter.LANGUAGE_CODE}}"

USE_TZ = True

TIME_ZONE = "{{cookiecutter.TIME_ZONE}}"
{% endif %}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
