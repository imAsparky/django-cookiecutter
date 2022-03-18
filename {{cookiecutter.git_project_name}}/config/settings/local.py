"""Django local settings for {{cookiecutter.git_project_name}} project."""

import environ

from .base import *  # noqa: F405 F401 F403

# Read from environment variables file
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env/.local"))  # noqa: F405

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DJANGO_DEBUG", default=False)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INTERNAL_IPS = env.list("INTERNAL_IPS")

EMAIL_BACKEND = env("EMAIL_BACKEND")


# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://github.com/node13h/django-debug-toolbar-template-profiler

# Django 4.0 does not support ugettext_lazy any more.
# Debug toolbar template profiler still requires ugettext_lazy.  Disabled until it runs on 4.0

# INSTALLED_APPS += ["template_profiler_panel"]  # noqa F405
INSTALLED_APPS += ["debug_toolbar", "django_browser_reload"]  # noqa F405

# Override the default logger level to the django environment
# log Level settings
LOGGING["loggers"][""]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL", default="DEBUG"
)  # noqa: F405
LOGGING["handlers"]["stdout"]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL", default="DEBUG"
)  # noqa: F405
LOGGING["handlers"]["rotated_logs"]["level"] = env(  # noqa F405
    "DJANGO_LOGGING_LEVEL", default="DEBUG"
)

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]  # noqa F405

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}
