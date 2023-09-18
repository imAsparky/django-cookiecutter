"""Django test settings for {{cookiecutter.git_project_name}} project."""

import environ
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F405 F401 F403

# Read from environment variables file
env = environ.FileAwareEnv(
    # set casting, default value
    DEBUG=(bool, True)
)
env.read_env(
    Path(BASE_DIR / ".env/.testing"),  # noqa: F405
)
logger = logging.getLogger(__name__)


ALLOWED_HOSTS = env.list(
    "TESTING_ALLOWED_HOSTS",
    default=["{{cookiecutter.ALLOWED_HOSTS}}"],
)

DEBUG = env("TESTING_DJANGO_DEBUG", default=False)


DJANGO_LOGGING_MAIL_ADMINS = env(
    "TESTING_DJANGO_LOGGING_MAIL_ADMINS",
    default="ERROR",
)

DJANGO_LOGGING_LEVEL = env(
    "TESTING_DJANGO_LOGGING_LEVEL",
    default="DEBUG",
)

DJANGO_LOG_FILE = env(
    "TESTING_DJANGO_LOG_FILE",
    default="logging/rotating_testing.log",
)

DJANGO_SETTINGS_MODULE = env(
    "TESTING_DJANGO_SETTINGS_MODULE",
    default="config.settings.test",
)

DJANGO_TEMPLATES_CSS = env(
    "TESTING_DJANGO_TEMPLATES_CSS",
    default="/static/css/styles.css",
)


# Selects which database to use for testing, default=sqlite3 .
TESTING_DATABASE = env(
    "TESTING_DJANGO_DATABASE",
    default="sqlite3",
)


if TESTING_DATABASE == "sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
        }
    }

else:
    DATABASES = {
        "default": env.db(
            "TESTING_DATABASE_URL",
        ),
    }


EMAIL_BACKEND = env(
    "TESTING_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)


# Default empty string required for Docker build to succeed.
EMAIL_HOST = env(
    "TESTING_EMAIL_HOST",
    default="",
)


EMAIL_HOST_PASSWORD = env(
    "TESTING_EMAIL_HOST_PASSWORD",
    default="",
)

EMAIL_HOST_USER = env(
    "TESTING_EMAIL_HOST_USER",
    default="",
)
EMAIL_PORT = env(
    "TESTING_EMAIL_PORT",
    default="",
)
EMAIL_USE_TLS = env(
    "TESTING_EMAIL_USE_TLS",
    default="",
)

INTERNAL_IPS = env.list(
    "TESTING_INTERNAL_IPS",
    default=["{{cookiecutter.INTERNAL_IPS}}"],
)

# Override the default logger level to the django environment
# log Level settings
LOGGING["loggers"][""]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["stdout"]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"][  # noqa: F405
    "level"
] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["filename"] = DJANGO_LOG_FILE  # noqa: F405


SECRET_KEY = env(
    "TESTING_DJANGO_SECRET_KEY",
    default="!!!INSECURE_TESTING_SECRET!!!",
)

# Check it is safe to run in testing.
assert (  # nosec
    SECRET_KEY != "!!!INSECURE_TESTING_SECRET!!!"
), "The DJANGO_SECRET_KEY must be set for testing."

TAILWIND_CSS_DEV = env(
    "TESTING_TAILWIND_CSS_DEV",
    default=False,
)
# `USE_STATIC` options are `local` or `S3`
USE_STATIC = env("TESTING_USE_STATIC", default="Local")

# Test with DEBUG off can speed up tests.
assert not settings.DEBUG, "DEBUG mode should be off for testing."  # nosec

DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

# https://docs.djangoproject.com/en/4.0/topics/testing/overview/#speeding-up-tests-auth-hashers
#
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]


try:
    # Digital Ocean S3 Storage Configuration
    if USE_STATIC == "S3":
        AWS_ACCESS_KEY_ID = env(
            "TESTING_AWS_ACCESS_KEY_ID",
            default="TESTING_AWS_KEY_NOT_SET",
        )
        AWS_SECRET_ACCESS_KEY = env(
            "TESTING_AWS_SECRET_ACCESS_KEY",
            default="TESTING_AWS_SECRET_NOT_SET",
        )

        AWS_S3_REGION_NAME = env(
            "TESTING_AWS_S3_REGION_NAME",
            default="syd1",
        )
        AWS_S3_ENDPOINT_URL = env(
            "TESTING_AWS_S3_ENDPOINT_URL",
            default=f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )
        AWS_STORAGE_BUCKET_NAME = env(
            "TESTING_AWS_STORAGE_BUCKET_NAME",
            default="tb-s3",
        )
        AWS_LOCATION = env(
            "TESTING_AWS_LOCATION",
            default=f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )
        # This isnt working when using an ENV VAR
        # AWS_S3_OBJECT_PARAMETERS = env(
        #     "TESTING_AWS_S3_OBJECT_PARAMETERS",
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
        STATIC_URL = env("TESTING_STATIC_URL", default="static-lo/")

        # Media url must end with default MEDIA_URL from env var or base.py added to
        # S3 storage location.
        MEDIA_URL = env("TESTING_MEDIA_URL", default="media-lo/")

        # Set the url for the css file
        TESTING_DJANGO_TEMPLATES_CSS = f"{STATIC_URL}css/styles.css"

    elif USE_STATIC != "S3":
        raise ImproperlyConfigured(
            "Testing environment USE_STATIC must be S3, it is configured to %s."
            % (USE_STATIC),
        )

except ImproperlyConfigured:
    logger.critical(
        "Testing environment USE_STATIC must be S3, it is configured to %s."
        % (USE_STATIC),
    )
