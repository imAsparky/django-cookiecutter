"""Initialise {{cookiecutter.git_project_name}} Core App Generic Views."""

from core.views.generic.base import HtmxTemplateView

from core.views.generic.detail import HtmxDetailView
from core.views.generic.edit import (
    HtmxCreateView,
    HtmxDeleteView,
    HtmxFormView,
    HtmxUpdateView,
)
from core.views.generic.list import HtmxListView

__all__ = [
    "HtmxCreateView",
    "HtmxDeleteView",
    "HtmxDetailView",
    "HtmxFormView",
    "HtmxListView",
    "HtmxTemplateView",
    "HtmxUpdateView",
    "HtmxGenericViewError",
]


class HtmxGenericViewError(Exception):
    """A problem in a generic view."""

    pass
