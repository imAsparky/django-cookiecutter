"""Django production settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa
from django.conf import settings

# Read from environment variables file
environ.Env.read_env(os.path.join(BASE_DIR, ".env/.production"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = ["{{cookiecutter.ALLOWED_HOSTS}}"]

# Check it is safe to run in producion.
assert not settings.Debug, "DEBUG mode should be off for production."  # nosec
assert (
    env("SECRET_KEY") != "!!!UNSECURE_PRODUCTION_SECRET!!!"
), "SECRET_KEY must be set for production."  # nosec
