"""Django local settings for {{cookiecutter.git_project_name}} project."""
import logging

# from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

import environ

from .base import *  # noqa: F405 F401 F403

# Read from environment variables file
env = environ.FileAwareEnv(
    # set casting, default value
    DEBUG=(bool, True)
)
env.read_env(
    Path(BASE_DIR / ".env/.local"),  # noqa: F405
)  # noqa: F405

logger = logging.getLogger(__name__)
{% if cookiecutter.ALLOWED_HOSTS == [] %}
ALLOWED_HOSTS = env.list(
    "LOCAL_ALLOWED_HOSTS",
    default=["127.0.0.1"],
)
{% else %}
ALLOWED_HOSTS = env.list(
    "LOCAL_ALLOWED_HOSTS",
    default=["{{cookiecutter.ALLOWED_HOSTS}}"],
)
{% endif %}

DEBUG = env("LOCAL_DJANGO_DEBUG", default=False)


DJANGO_LOGGING_MAIL_ADMINS = env(
    "LOCAL_DJANGO_LOGGING_MAIL_ADMINS",
    default="ERROR",
)

DJANGO_LOGGING_LEVEL = env(
    "LOCAL_DJANGO_LOGGING_LEVEL",
    default="DEBUG",
)

DJANGO_LOG_FILE = env(
    "LOCAL_DJANGO_LOG_FILE",
    default="logging/rotating.log",
)

DJANGO_SETTINGS_MODULE = env(
    "LOCAL_DJANGO_SETTINGS_MODULE",
    default="config.settings.local",
)

DJANGO_TEMPLATES_CSS = env(
    "LOCAL_DJANGO_TEMPLATES_CSS",
    default="/static/css/styles.css",
)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

EMAIL_BACKEND = env(
    "LOCAL_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)


# Default empty string required for Docker build to succeed.
EMAIL_HOST = env(
    "LOCAL_EMAIL_HOST",
    default="",
)


EMAIL_HOST_PASSWORD = env(
    "LOCAL_EMAIL_HOST_PASSWORD",
    default="",
)

EMAIL_HOST_USER = env(
    "LOCAL_EMAIL_HOST_USER",
    default="",
)
EMAIL_PORT = env(
    "LOCAL_EMAIL_PORT",
    default="",
)
EMAIL_USE_TLS = env(
    "LOCAL_EMAIL_USE_TLS",
    default="",
)

INSTALLED_APPS += [  # noqa: F405
    "django_browser_reload",
    "debug_toolbar",
]
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    # "template_profiler_panel.panels.template.TemplateProfilerPanel",
]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}


INTERNAL_IPS = env.list(
    "LOCAL_DJANGO_INTERNAL_IPS",
    default=["{{cookiecutter.INTERNAL_IPS}}"],
)

# Override the default logger level to the django environment
# log Level settings
LOGGING["loggers"][""]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["stdout"]["level"] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"][
    "level"
] = DJANGO_LOGGING_LEVEL  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["filename"] = DJANGO_LOG_FILE  # noqa: F405

MIDDLEWARE += [  # noqa: F405
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

SECRET_KEY = env(
    "LOCAL_DJANGO_SECRET_KEY",
    default="!!!INSECURE_LOCAL_SECRET!!!",
)


# Check it is safe to run in local.
assert (  # nosec
    env("LOCAL_DJANGO_SECRET_KEY") != "!!!INSECURE_LOCAL_SECRET!!!"
), "The DJANGO_SECRET_KEY must be set for local."

TAILWIND_CSS_DEV = env(
    "LOCAL_TAILWIND_CSS_DEV",
    default=True,
)


# `USE_STATIC` options are `Local` or `S3`
USE_STATIC = env("LOCAL_USE_STATIC", default="Local")

# Digital Ocean S3 Storage Configuration
if USE_STATIC == "S3":
    AWS_ACCESS_KEY_ID = env(
        "LOCAL_AWS_ACCESS_KEY_ID",
        default="LOCAL_AWS_KEY_NOT_SET",
    )
    AWS_SECRET_ACCESS_KEY = env(
        "LOCAL_AWS_SECRET_ACCESS_KEY",
        default="LOCAL_AWS_SECRET_NOT_SET",
    )

    AWS_S3_REGION_NAME = env(
        "LOCAL_AWS_S3_REGION_NAME",
        default="syd1",
    )
    AWS_S3_ENDPOINT_URL = env(
        "LOCAL_AWS_S3_ENDPOINT_URL",
        default=f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
    )
    AWS_STORAGE_BUCKET_NAME = env(
        "LOCAL_AWS_STORAGE_BUCKET_NAME",
        default="tb-s3",
    )
    AWS_LOCATION = env(
        "LOCAL_AWS_LOCATION",
        default=f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
    )
    # This isnt working when using an ENV VAR
    # AWS_S3_OBJECT_PARAMETERS = env(
    #     "LOCAL_AWS_S3_OBJECT_PARAMETERS",
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
    STATIC_URL = env("LOCAL_STATIC_URL", default="static-lo/")

    # Media url must end with default MEDIA_URL from env var or base.py added to
    # S3 storage location.
    MEDIA_URL = env("LOCAL_MEDIA_URL", default="media-lo/")

    # Set the url for the css file
    LOCAL_DJANGO_TEMPLATES_CSS = f"{STATIC_URL}css/styles.css"

#     elif USE_STATIC != "S3":
#         raise ImproperlyConfigured(
#             "Staging environment USE_STATIC must be S3, it is configured to %s."
#             % (USE_STATIC),
#         )

# except ImproperlyConfigured:
#     logger.critical(
#         "Staging environment USE_STATIC must be S3, it is configured to %s."
#         % (USE_STATIC),
#     )
