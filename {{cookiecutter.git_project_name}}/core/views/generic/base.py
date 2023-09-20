"""{{cookiecutter.git_project_name}} Core App Generic Views Base."""

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin, TemplateView


class HtmxTemplateResponseMixin(TemplateResponseMixin):
    """Extends Django TemplateResponseMixin with HTMX functionality.

    Renders an htmx template or a generic template response.

    MIT License

    Copyright (c) 2021 Pablo Rivera

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    htmx_template_name = None

    def get_template_names(self):
        """Return a list of template names.

        May not be called if render_to_response() is overridden.
        """
        super().get_template_names()

        if self.template_name is None or self.htmx_template_name is None:
            raise ImproperlyConfigured(
                "HtmxTemplateResponseMixin requires either a definition of "
                "'htmx_template_name' and 'template_name' or an "
                "implementation of 'get_template_names()'"
            )

        if self.request.htmx:
            return [self.htmx_template_name]

        return [self.template_name]


class HtmxTemplateView(HtmxTemplateResponseMixin, TemplateView):
    """Extends Django Template View with HTMX functionality.

    Renders an htmx template or a generic template response.
    """

    def get(self, request, *args, **kwargs):
        """Extends GET to check if the user has defined the
        'not_htmx_request_redirect' attribute. If they have
        and the request is not using HTMX then redirect the
        user to the value of the attribute.
        """
        if hasattr(self, "not_htmx_request_redirect"):
            if request.htmx:
                return super().get(self, request, *args, **kwargs)
            else:
                return redirect(self.not_htmx_request_redirect)
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Extends POST to check if the user has defined the
        'not_htmx_request_redirect' attribute. If they have
        and the request is not using HTMX then redirect the
        user to the value of the attribute.
        """
        if hasattr(self, "not_htmx_request_redirect"):
            if request.htmx:
                return super().post(self, request, *args, **kwargs)
            else:
                return redirect(self.not_htmx_request_redirect)
        return super().post(self, request, *args, **kwargs)
