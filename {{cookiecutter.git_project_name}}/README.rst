=================================
**{{cookiecutter.project_name}}**
=================================

*{{cookiecutter.project_short_description}}*

{%- if cookiecutter.use_repo_status_badge != "no" %}
.. image:: https://www.repostatus.org/badges/latest/{{cookiecutter.use_repo_status_badge}}.svg
   :target: https://www.repostatus.org/#concept
   :alt: Project Status: Concept
{%- endif %}

{%- if cookiecutter.use_pre_commit == "y" %}
.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
{%- endif %}

{%- if cookiecutter.open_source_license != "Not open source" %}
:License: {{cookiecutter.open_source_license}}
{%- endif %}














Built with
`Django Cookicutter <https://github.com/imAsparky/django-cookiecutter>`_
