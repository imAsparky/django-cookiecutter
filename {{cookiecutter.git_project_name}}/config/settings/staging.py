"""Django staging settings for {{cookiecutter.git_project_name}} project."""

import environ
from django.conf import settings

from .base import *  # noqa: F405 F401 F403
{% if cookiecutter.deploy_with_docker == "swarm" %}
env = environ.FileAwareEnv()
{% else %}
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env/.staging"))  # noqa: F405
{% endif %}
# fmt: off
SECRET_KEY = env('DJANGO_SECRET_KEY', default="!!!INSECURE_PRODUCTION_SECRET!!!")

DEBUG = env('DJANGO_DEBUG', default=False)
# fmt: on

ALLOWED_HOSTS = ["{{cookiecutter.ALLOWED_HOSTS}}"]

INTERNAL_IPS = ["{{cookiecutter.INTERNAL_IPS}}"]

EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

DATABASES = {"default": env.db()}

# Override the default logger level to the django environment
# log Level settings
LOGGING["loggers"][""]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL_STAGING", default="WARNING"
)  # noqa: F405
LOGGING["handlers"]["stdout"]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL_STAGING", default="WARNING"
)  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL_STAGING", default="WARNING"
)


# Check it is safe to run in production.
assert (  # nosec
    not settings.DEBUG
), "DEBUG mode should be False for the production environment."
assert (  # nosec
    env("DJANGO_SECRET_KEY") != "!!!INSECURE_PRODUCTION_SECRET!!!"
), "The DJANGO_SECRET_KEY must be set for production."
