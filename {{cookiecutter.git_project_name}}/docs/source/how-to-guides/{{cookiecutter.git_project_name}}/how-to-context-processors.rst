.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-context-processors ; Index


.. _how-to-context-processors:

====================
Context Procecessors
====================

|

{{ cookiecutter.project_name }} `context_processors` are located in `core/utils/context_processors.py`


Exporting Variables
===================

|

There are times when making `Environment`, or other `Variables`` easily and consistently
accessible in `html` templates.

|

Adding a variable
-----------------
|

See below for existing config as an example of how to add a variable to the context.

.. code-block:: python

    import environ
    from constance import config

    env = environ.FileAwareEnv()

    def export_vars(request) -> dict:

    data: dict = {}

    data["CSS"] = env("DJANGO_TEMPLATES_CSS", default="static/css/styles.css")
    data["TAILWIND_CSS_DEV"] = env("TAILWIND_CSS_DEV", default=False)
    data["ALLOW_NEW_USER_SIGNUP"] = config.ALLOW_NEW_USER_SIGNUP

    return data

|

Useage in HTML
--------------
|

See below for existing HTML as an example of how to use a variable supplied in the context.

|

.. code-block:: html

    {% raw %}
    {% if not TAILWIND_CSS_DEV %}
    <link rel="stylesheet" href="{{ CSS }}">
    {% endif %}

    {% if TAILWIND_CSS_DEV %}
      {% tailwind_css %}
      <p> TAILWIND {{ TAILWIND_CSS_DEV}}</p>
    {% endif %}
    {% endraw %}
