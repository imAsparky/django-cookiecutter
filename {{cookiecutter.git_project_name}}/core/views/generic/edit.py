"""{{cookiecutter.git_project_name}} Core App Generic Views Edit."""

from django.views.generic import CreateView, DeleteView, FormView, UpdateView

from core.views.generic.base import HtmxTemplateResponseMixin


class HtmxCreateView(HtmxTemplateResponseMixin, CreateView):
    """Extends Django List view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """


class HtmxDeleteView(HtmxTemplateResponseMixin, DeleteView):
    """Extends Django Delete view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """


class HtmxFormView(HtmxTemplateResponseMixin, FormView):
    """Extends Django Form view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """


class HtmxUpdateView(HtmxTemplateResponseMixin, UpdateView):
    """Extends Django Update view with HTMX functionality.

    Renders an htmx template or a generic template response.
    """
