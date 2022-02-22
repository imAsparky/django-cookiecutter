"""{{cookiecutter.git_project_name}} Core App Generic Views List."""

from django.views.generic import ListView

from core.views.generic.base import HtmxTemplateResponseMixin


class HtmxListView(HtmxTemplateResponseMixin, ListView):
    """Extends Django List view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """
