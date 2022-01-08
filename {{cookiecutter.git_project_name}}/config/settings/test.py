"""Django test settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa
from django.conf import settings
import environ

# Read from environment variables file
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env/.testing"))

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = [""]

INTERNAL_IPS = [""]


# Selects which database to use for testing, default=sqlite3 .
TESTING_DATABASE = env("TESTING_DATABASE")

if TESTING_DATABASE == "sqlite3":

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            # "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:

    DATABASES = {"default": env.db()}

# Test with DEBUG off can speed up tests.
assert not settings.DEBUG, "DEBUG mode should be off for testing."  # nosec

DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

# https://docs.djangoproject.com/en/3.2/topics/testing/overview/#speeding-up-tests-auth-hashers
#
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
