.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-htmx ; Index

.. _how-to-htmx:
====
HTMX
====

See `django-htmx` [#]_ for detailed information about using django-htmx in your
django-cookiecutter project.


Class Base Views
----------------

django-cookiecutter has used a similar approach to Class-Based Views as the
Django standard libray.  Importing HTMX enabled Generic Views is as straight
forward as Django but comes from django-cookiecutter `core`.
The htmx views are mixins using htmx and django views.


HTMX
~~~~

All of Django Generic Edit, List and Detail Views are available from
`core.views.generic`.


.. code-block:: python
    :linenos:

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


|

A simple htmx create view.

.. code-block:: python
    :linenos:

    from core.views.generic import HtmxCreateView
    from .forms import YourForm
    from .models import YourModel

    class YourHtmxCreateView(HtmxCreateView):
        """Your HTMX Create View"""
        form_class = YourForm
        model = YourModel
        htmx_template_name = "your/htmx/partial/template.html"
        template_name = "your/standard/django/template.html"
        success_url = reverse_lazy("your_success_url")

        def your_code_here(self):


Django
------

All of Django Generic Edit, List and Detail Views are still available from
Django standard library if you prefer to use those in some cases.

.. code-block:: python
    :linenos:

    from django.views.generic import CreateView
    from .forms import YourForm
    from .models import YourModel

    class YourCreateView(CreateView):
        """Your Django Create View"""
        form_class = YourForm
        model = YourModel
        template_name = "your/standard/django/template.html"
        success_url = reverse_lazy("your_success_url")

        def your_code_here(self):


HTMX Function View
------------------


An example taken from `django-htmx examples` [#]_.

.. code-block:: python
    :linenos:

    @require_GET
    def partial_rendering(request: HttpRequest) -> HttpResponse:
        # Standard Django pagination
        page_num = request.GET.get("page", "1")
        page = Paginator(object_list=people, per_page=10).get_page(page_num)

        # The htmx magic - use a different, minimal base template for htmx
        # requests, allowing us to skip rendering the unchanging parts of the
        # template.
        if request.htmx:
            base_template = "_partial.html"
        else:
            base_template = "_base.html"

        return render(
            request,
            "partial-rendering.html",
            {
                "base_template": base_template,
                "page": page,
            },
        )


HTMX CSRF in HTML
-----------------

HTMX uses HTTP methods other than `GET`. Django expects a CSRF security token
in the request; otherwise, Django will respond to the request with a
`403 Forbidden` status code.

Htmx looks to parent elements for additional attributes; you can apply the CSRF
token for HTMX methods globally by including the `hx-headers` in the body tag,
as shown below.

This CSRF method is taken from  Matt Laymans blog `How To Use Htmx In Django` [#]_.
See Matt's blog for another technique to add CSRF tokens.

.. code-block:: html
    :linenos:

    <html>

        <head><title>HTML Base file</title></head>

        <body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>
            {% block main %}{% endblock %}
            <script src="https://unpkg.com/htmx.org@1.1.0"></script>
        </body>

    </html>

|

Further Reading
---------------

A fantastic list of htmx examples on `htmx.org` [#]_.

An excellent YouTube Django HTMX series by `BUGBYTES` [#]_.

|

.. rubric:: Footnotes

.. [#] https://github.com/adamchainz/django-htmx
.. [#] https://github.com/adamchainz/django-htmx/blob/main/example/example/core/views.py
.. [#] https://www.mattlayman.com/blog/2021/how-to-htmx-django/
.. [#] https://htmx.org/examples/
.. [#] https://www.youtube.com/watch?v=Ula0c_rZ6gk&list=PL-2EBeDYMIbRByZ8GXhcnQSuv2dog4JxY
