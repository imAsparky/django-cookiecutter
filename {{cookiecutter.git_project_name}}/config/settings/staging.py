"""Django staging settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa
from django.conf import settings
import environ
{% if cookiecutter.deploy_with_docker == "swarm" %}
env = environ.FileAwareEnv()
{% else %}
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env/.staging"))
{% endif %}
# fmt: off
SECRET_KEY = env('DJANGO_SECRET_KEY', default="!!!INSECURE_PRODUCTION_SECRET!!!")

DEBUG = env('DJANGO_DEBUG', default=False)
# fmt: on

ALLOWED_HOSTS = ["{{cookiecutter.ALLOWED_HOSTS}}"]
ALLOWED_HOSTS += ["139.59.102.221", "127.0.0.1"]

INTERNAL_IPS = env.list("INTERNAL_IPS", default=["127.0.0.1", "10.0.2.2"])

EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

DATABASES = {"default": env.db()}

# Check it is safe to run in producion.
assert (
    not settings.DEBUG
), "DEBUG mode should be off for the production environment."  # nosec
assert (
    env("DJANGO_SECRET_KEY") != "!!!INSECURE_PRODUCTION_SECRET!!!"
), "The DJANGO_SECRET_KEY must be set for production."  # nosec
