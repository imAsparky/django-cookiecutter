"""Django test settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa

# https://docs.djangoproject.com/en/3.2/topics/testing/overview/#speeding-up-tests-auth-hashers
#
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
