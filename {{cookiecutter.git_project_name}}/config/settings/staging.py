"""Django staging settings for {{cookiecutter.git_project_name}} project."""

import environ
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

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
logger = logging.getLogger(__name__)


ALLOWED_HOSTS = env.list(
    "STAGING_ALLOWED_HOSTS",
    default=["{{cookiecutter.ALLOWED_HOSTS}}"],
)

DEBUG = env("STAGING_DJANGO_DEBUG", default=False)


DJANGO_LOGGING_MAIL_ADMINS = env(
    "STAGING_DJANGO_LOGGING_MAIL_ADMINS",
    default="ERROR",
)

DJANGO_LOGGING_LEVEL = env(
    "STAGING_DJANGO_LOGGING_LEVEL",
    default="INFO",
)

DJANGO_LOG_FILE = env(
    "STAGING_DJANGO_LOG_FILE",
    default="logging/rotating.log",
)

DJANGO_SETTINGS_MODULE = env(
    "STAGING_DJANGO_SETTINGS_MODULE",
    default="config.settings.staging",
)


DATABASES = {
    "default": env.db(
        "STAGING_DATABASE_URL",
    ),
}

EMAIL_BACKEND = env(
    "STAGING_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)


# Default empty string required for Docker build to succeed.
EMAIL_HOST = env(
    "STAGING_EMAIL_HOST",
    default="",
)


EMAIL_HOST_PASSWORD = env(
    "STAGING_EMAIL_HOST_PASSWORD",
    default="",
)

EMAIL_HOST_USER = env(
    "STAGING_EMAIL_HOST_USER",
    default="",
)
EMAIL_PORT = env(
    "STAGING_EMAIL_PORT",
    default="",
)
EMAIL_USE_TLS = env(
    "STAGING_EMAIL_USE_TLS",
    default="",
)

INTERNAL_IPS = env.list(
    "STAGING_INTERNAL_IPS",
    default=["{{cookiecutter.INTERNAL_IPS}}"],
)

# Override the default logger level to the django environment
# log Level settings
LOGGING["loggers"][""]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["stdout"]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["filename"] = DJANGO_LOG_FILE  # noqa: F405


SECRET_KEY = env(
    "STAGING_DJANGO_SECRET_KEY",
    default="!!!INSECURE_STAGING_SECRET!!!",
)


# Check it is safe to run in staging.
assert (  # nosec
    env("STAGING_DJANGO_SECRET_KEY") != "!!!INSECURE_STAGING_SECRET!!!"
), "The DJANGO_SECRET_KEY must be set for staging."


# `USE_STATIC` options are `local` or `S3`
USE_STATIC = env("STAGING_USE_STATIC", default="Local")


try:
    # Digital Ocean S3 Storage Configuration
    if USE_STATIC == "S3":
        AWS_ACCESS_KEY_ID = env(
            "STAGING_AWS_ACCESS_KEY_ID",
            default="STAGING_AWS_KEY_NOT_SET",
        )
        AWS_SECRET_ACCESS_KEY = env(
            "STAGING_AWS_SECRET_ACCESS_KEY",
            default="STAGING_AWS_SECRET_NOT_SET",
        )

        AWS_S3_REGION_NAME = env(
            "STAGING_AWS_S3_REGION_NAME",
            default="syd1",
        )
        AWS_S3_ENDPOINT_URL = env(
            "STAGING_AWS_S3_ENDPOINT_URL",
            default=f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )
        AWS_STORAGE_BUCKET_NAME = env(
            "STAGING_AWS_STORAGE_BUCKET_NAME",
            default="tb-s3",
        )
        AWS_LOCATION = env(
            "STAGING_AWS_LOCATION",
            default=f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )
        # This isnt working when using an ENV VAR
        # AWS_S3_OBJECT_PARAMETERS = env(
        #     "STAGING_AWS_S3_OBJECT_PARAMETERS",
        #     {"CacheControl": "max-age=1"},
        # )
        AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=1"}

        STORAGES = {
            "default": {
                "BACKEND": env(
                    "DEFAULT_FILE_STORAGE",
                    default="core.storage.backends.MediaRootS3Boto3Storage",
                )
            },
            "staticfiles": {
                "BACKEND": env(
                    "STATICFILES_STORAGE",
                    default="core.storage.backends.StaticRootS3Boto3Storage",
                )
            },
        }

        # Static url must end with default STATIC_URL from env var or base.py added to
        # S3 storage location.

        STATIC_URL = env("STAGING_STATIC_URL", default="static-st/")

        # Media url must end with default MEDIA_URL from env var or base.py added to
        # S3 storage location.
        MEDIA_URL = env("STAGING_MEDIA_URL", default="media-st/")

        # Set the url for the css file
        STAGING_DJANGO_TEMPLATES_CSS = f"{STATIC_URL}css/styles.css"

    elif USE_STATIC != "S3":
        raise ImproperlyConfigured(
            "Staging environment USE_STATIC must be S3, it is configured to %s."
            % (USE_STATIC),
        )

except ImproperlyConfigured:
    logger.critical(
        "Staging environment USE_STATIC must be S3, it is configured to %s."
        % (USE_STATIC),
    )
