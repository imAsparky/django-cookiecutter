============================
**Django 4.0+ Cookiecutter**
============================

**Version = "0.29.0"**

**Version 1.0.0 will signify the first stable Django build!**

**This cookiecutter uses django-tailwind by default.  django-tailwind requires
Node.js be installed on your development machine.**

.. image:: ./docs/source/_static/imgs/logo/logo-django-cookiecutter-1280x640.png
   :alt:

A `Django`_  project `Cookiecutter`_ complete with built-in continuous
delivery using GitHub actions.

.. _Django: https://www.djangoproject.com/
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter

.. image:: https://www.repostatus.org/badges/latest/wip.svg
   :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
   :target: https://www.repostatus.org/#wip

.. image:: https://app.codacy.com/project/badge/Grade/87fb6c8ef02d4433b87e483a9a926d62
   :alt: Codacy Quality
   :target: https://www.codacy.com/gh/imAsparky/django-cookiecutter/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=imAsparky/django-cookiecutter&amp;utm_campaign=Badge_Grade

.. image:: https://pyup.io/repos/github/imAsparky/django-cookiecutter/shield.svg
     :target: https://pyup.io/repos/github/imAsparky/django-cookiecutter/
     :alt: Updates

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

.. image:: https://readthedocs.org/projects/django-cookiecutter/badge/?version=latest
   :target: https://django-cookiecutter.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg
   :target: https://python-semantic-release.readthedocs.io/en/latest/
   :alt: Python Sementic Release

Django Project Features
-----------------------

#. Easy for new users to learn Django with sensible defaults.  Also, `local`
   and `test` environments default to using `SQLite`_, Django's bundled
   database.
#. More advanced users can change the test environment database with an
   environment variable to match the production environment. See the How-to `here`_.
#. `Django-allauth`_ provides authentication.
#. A `CustomUser` model, complete with tests and custom user types. See
   `How-to Custom User`_ for customisation options before your initial migration.
#. Improved  Admin panel security requires an authorised user to be logged in.
   The Admin panel now has the protections provided by django-allauth.
#. `htmx`_ built in by default using `django-htmx`_.
#. `django-tailwind`_ and `django-browser-reload`_ built in by default.
#. Customisable logging with rotating log files, see `how-to-logging`_.

If you are new to Django and Cookiecutters and would like to take it for a spin,
see our tutorial, `Create a Django-Cookiecutter Project`_.


.. _Django-allauth: https://django-allauth.readthedocs.io/en/latest/installation.html
.. _SQLite: https://www.sqlite.org/index.html
.. _How-to Custom User: https://django-cookiecutter.readthedocs.io/en/latest/how-tos/how-to-custom-user.html
.. _here: https://django-cookiecutter.readthedocs.io/en/latest/how-tos/how-to-test-env-settings.html
.. _Create a Django-Cookiecutter Project: https://django-cookiecutter.readthedocs.io/en/latest/tutorials/tutorial-create-django-project.html
.. _htmx: https://htmx.org/
.. _django-htmx: https://github.com/adamchainz/django-htmx
.. _django-tailwind: https://github.com/timonweb/django-tailwind
.. _django-browser-reload: https://github.com/adamchainz/django-browser-reload
.. _how-to-logging: https://django-cookiecutter.readthedocs.io/en/latest/how-tos/how-to-logging.html

Django Project Creation Options
-------------------------------

Customise your project with the following options when creating your
django-cookiecutter.

If you are new to Django and arent sure what to select, choose the default
setting to get the best new user experience.

Django Settings
~~~~~~~~~~~~~~~

#. Quickly configure common `Django settings`_ as you setup your project.

.. _Django settings: https://docs.djangoproject.com/en/4.0/ref/settings/

Docker
~~~~~~

#. Deploy to production with `Docker`_.

.. _Docker: https://www.docker.com/


Documentation
~~~~~~~~~~~~~

#. Add documentation using Sphinx with:

   #. `Furo`_, a clean modern theme,  with dark and light mode options.
   #. A `Copy Button`_ to assist your users copy text or code snippets.
   #. `Inline Tabs`_ to group similar items.
   #. Use markdown or restructured text.
#. Deploy to `Read the Docs`_.
#. A documentation framework with templates using the `Diátaxis framework`_
#. A Pre-generated Contributing How-to. Edit to suit your needs.

.. _Diátaxis framework: https://junction-box.readthedocs.io/en/latest/Document-Framework/diataxis-intro.html

GitHub Helpers
~~~~~~~~~~~~~~

#. A set of four custom GitHub Issues templates to help your users.
#. Create the local git repository and make the initial commit automatically.
#. A `Conventional commits`_
   style custom commits message template.

.. _Conventional commits: https://www.conventionalcommits.org/en/v1.0.0/

Workflow Helpers
~~~~~~~~~~~~~~~~

#. Pre-commit for code quality help and a README badge.
#. A Python Semantic Release GitHub action and a README badge.
#. A test suite complete with py3.8-py3.10, Linux, macOS and Windows matrix.

Communication
~~~~~~~~~~~~~

#. Choose from five LICENSE types for open source projects.
#. Choose from three `Repository Status Badges`_.
   Quickly communicate to potential users.


.. _Furo: https://github.com/pradyunsg/furo
.. _Copy Button: https://sphinx-copybutton.readthedocs.io/en/latest/
.. _Inline Tabs: https://sphinx-inline-tabs.readthedocs.io/en/latest/
.. _Read the Docs: https://readthedocs.org/
.. _Repository Status Badges: https://www.repostatus.org/#concept

Dynamic Settings
~~~~~~~~~~~~~~~~

Choose to add `django-constance`_ for dynamic Django settings, which allows
you to:

#. Easily migrate your static settings to dynamic settings.
#. Edit dynamic settings in the Django Admin interface.

See our `django-constance How-to`_  for more information.

.. _django-constance: https://django-constance.readthedocs.io/en/latest/index.html
.. _django-constance How-to: https://django-cookiecutter.readthedocs.io/en/latest/how-tos/how-to-constance.html

Contributing
------------

Contributions are very welcome and appreciated!

You can contribute in many ways.

See `How-to Contribute <https://django-cookiecutter.readthedocs.io/en/
latest/how-tos/how-to-contribute.html>`_ to help you get started.

Please take a moment to read our `Code of Conduct
<https://django-cookiecutter.readthedocs.io/en/latest/
code-of-conduct.html#code-of-conduct>`_.
