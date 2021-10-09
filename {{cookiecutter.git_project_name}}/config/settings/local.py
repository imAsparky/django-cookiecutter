"""Django local settings for {{cookiecutter.git_project_name}} project."""

from .base import *  # noqa

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "!!!SET DJANGO_SECRET_KEY!!!")

DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://github.com/node13h/django-debug-toolbar-template-profiler

INSTALLED_APPS += ["debug_toolbar", "template_profiler_panel"]  # noqa F405


MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405


DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}

DEBUG_TOOLBAR_PANELS = [
    # ...
    "template_profiler_panel.panels.template.TemplateProfilerPanel",
]

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
