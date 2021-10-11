"""Django test settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa
from django.conf import settings

DEBUG = False

assert not settings.Debug, "DEBUG mode should be off"  # nosec

# https://docs.djangoproject.com/en/3.2/topics/testing/overview/#speeding-up-tests-auth-hashers
#
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
