"""{{cookiecutter.git_project_name}} Core App Generic Views Detail."""

from django.views.generic import DetailView

from core.views.generic.base import HtmxTemplateResponseMixin


class HtmxDetailView(HtmxTemplateResponseMixin, DetailView):
    """Extends Django Detail view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """
