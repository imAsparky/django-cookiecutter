=================================
**{{cookiecutter.project_name}}**
=================================

*{{cookiecutter.project_short_description}}*

{%- if cookiecutter.use_repo_status_badge != "no" %}
.. image:: https://www.repostatus.org/badges/latest/{{cookiecutter.use_repo_status_badge}}.svg
   :target: https://www.repostatus.org/#{{cookiecutter.use_repo_status_badge}}
   :alt: Project Status: {{cookiecutter.use_repo_status_badge}}
{%- endif %}

{%- if cookiecutter.use_pre_commit == "y" %}
.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
{%- endif %}

{%- if cookiecutter.use_GH_action_semantic_version == "y" %}
.. image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg
   :target: https://python-semantic-release.readthedocs.io/en/latest/
   :alt: Python Sementic Release
{%- endif %}

{%- if cookiecutter.use_readthedocs == "y" %}
.. image:: https://readthedocs.org/projects/{{cookiecutter.git_project_name}}/badge/?version=latest
   :target: https://{{cookiecutter.git_project_name}}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
{%- endif %}

{%- if cookiecutter.open_source_license != "Not open source" %}
:License: {{cookiecutter.open_source_license}}
{%- endif %}














Built with
`Django Cookicutter <https://github.com/imAsparky/django-cookiecutter>`_
