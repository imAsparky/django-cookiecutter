.. highlight:: rst
.. index:: settings-discussion ; Index


.. _settings-discussion:
=============================
Django Settings Best Practice
=============================

Although there are many ways to configure the Django settings file structures,
there is a commonality in many experienced developers' approaches or preferred
guidelines.

#. Keep Secret keys out of Version Control.
#. Version control settings.
#. Follow The 12 Factor App [#]_ principles of storing Config.
#. Do not repeat yourself.
#. Keep Secret keys out of Version Control [#]_.

The 12 Factor guideline focus of this discussion is number three Config.

By following this guideline, we ensure strict separation between configuration
settings and code.

Extract from 12 Factor Config: [#]_
-----------------------------------

*An app's config is everything likely to vary between deploys (staging,
production, developer environments, etc.).*

*A litmus test for whether an app has all config correctly factored out of the
code is whether the codebase could be made open source at any moment without compromising any credentials.*


Naming Conventions
------------------

Poor naming practices can lead to potential errors and lost time.  The result
can often be frustrating.

Naming variables and settings is a challenging part of development. Following
this simple guide for your custom project settings can make this a
little easier:

#. Give meaningful names to your settings.
#. Use the project name as a prefix to your custom project settings.
#. Write meaningful descriptions for your settings in the comments.

.. admonition:: **A meaningful setting name with comments.**

    .. code-block:: python

        # The default widget colour.
        # Accepts a hex colour value.
        MY_DJANGO_PROJECT_WIDGET_DEFAULT_COLOUR = #ff0000

Settings Files Structure
------------------------

From the outset, having a good configuration file structure has many benefits
as the project grows. Some key benefits are:

#. Separation of concerns; see file structure below.
#. The settings are DRY [#]_.
#. Eliminate copy and paste of settings.
#. Eliminate errors with local dev settings breaking production.
#. The settings file size is smaller and more manageable.

Django Cookiecutter will follow the settings file layout described in
Two Scoops of Django 3.x [#]_.

.. code-block:: python
   :caption: **Settings File Structure**

    config
     └── settings
          ├── __init__.py
          ├── base.py
          ├── local.py
          ├── production.py
          ├── staging.py
          └── test.py


.. rubric:: Footnotes

.. [#] https://12factor.net/
.. [#] https://12factor.net/config
.. [#] A little bit of irony to get the point across.
.. [#] https://www.feldroy.com/books/two-scoops-of-django-3-x
.. [#] **D** o not **R** epeat **Y** ourself
