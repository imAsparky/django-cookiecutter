.. highlight:: rst
.. index:: django-proj-inputs ; Index

.. _project-inputs:
==================
New Project Inputs
==================


A new Django Cookiecutter Project requires some information to customise your
new project.  If unsure, choose the default option.

Project Level Inputs
--------------------

The following items appear in various parts of your Django Project.

author_name
~~~~~~~~~~~

Your full name.

email
~~~~~

Your email address.

github_username
~~~~~~~~~~~~~~~

Your GitHub username.

project_name
~~~~~~~~~~~~

The name of your new Django project,  used in the documentation,
so spaces and any characters are acceptable here.

git_project_name
~~~~~~~~~~~~~~~~

Your previously created GitHub project repository name.

If it is the same as your project_name but with hyphens instead of spaces,
leave this blank.  Cookiecutter will generate your GitHub repository name
with hyphens.

If it is different to your project name, enter your  GitHub repository here.

project_slug
~~~~~~~~~~~~

project_slug is the namespace of your Django project. The project_slug should
be Python import-friendly.  Typically, it is the slugified version of
project_name.

project_short_description
~~~~~~~~~~~~~~~~~~~~~~~~~

A  sentence describes your Django project.

version
~~~~~~~

The first version number.  The version number appears in the documentation
and semantic version release.


Options
-------

The following Django Cookiecutter configuration options are grouped logically.

Where options are in a list, the first item is the default setting.

GitHub Tools
-------------


.. caution::

    **Initialise your local git requires Git v2.33.0 or above.**

"automatic_set_up_git_and_initial_commit": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatically create the local repository and make the first commit after
your project generation.

You can check this on the command line with

.. code-block:: bash
    git reflog

"create_conventional_commits_edit_message": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a commit message template in the style of `Conventional Commits`_ .

.. important::

    If you choose yes, and are NOT using  "automatic_set_up_git_and_initial_commit" run the following command after manually
    initiating git to let git know you are using a custom template.

    .. code-block:: bash

        git config --local commit.template .github/.git-commit-template.txt

"use_GH_custom_issue_templates": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Four custom GitHub issue templates to assist users in providing the
necessary information. Templates are

#. Bug Report.
#. Feature Request.
#. Documentation Request.
#. Chore Request.

See the typical template markdown file settings below for a feature request.

.. code-block:: yaml

    ---
    name: Feature request
    about: Suggest an idea for this project
    title: "[FEAT]:"
    labels: enhancement
    assignees: { { cookiecutter.github_username } }
    ---

If you prefer, a simple issue template is available for use with all
issues if you choose `no` for this feature.


Workflow Tools
--------------

"use_pre_commit": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use pre-commit with some sensible options.  Configure to your needs after
project generation.

"create_repo_auto_test_workflow": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tox testing is built-in.  Use this workflow, and GitHub protected branches,
to ensure all contributed code passes the test suite before it can merge with
your main branch.

"use_GH_action_semantic_version": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this GitHub workflow to automatically update the semantic version number
after a merge to the main branch.  The semantic version utilises Python
Semantic Release.  This workflow requires a GitHub secret key, `SEM_VER`.

Django Settings
---------------

"ALLOWED_HOSTS": "www.example.com",

"INTERNAL_IPS": "127.0.0.1",

"LANGUAGE_CODE": "en-au",

"LANGUAGES": "hi",

"TIME_ZONE": "UTC",

"USE_L10N": "True",

"USE_I18N": "True",

"SITE_ID": "1",

See `Django Settings`_ for more information.

Documentation
---------------

"include_sphinx_docs": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include Sphinx documentation folder structure and tools to
generate documentation.

"use_readthedocs": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy your documentation to Read the Docs.  Includes generating a badge on
your README.

"include_documentation_templates":["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Diátaxis`_ framework templated documentation.  sections with index's.

"include_how_to_contribute_template":["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A completed How-To contribute template that only needs fine-tuning to your
contributing requirements.

"include_contributor_covenant_code_of_conduct":["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include a code of conduct.

Communication
-------------

"use_repo_status_badge": ["no", "concept", "wip", "active"]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let people know what stage your Django project is with a README badge.

"use_pyup_io": ["y", "n"]
~~~~~~~~~~~~~~~~~~~~~~~~~

Let people know your dependency status with a README badge.
Requires a `Pyup.io`_ account linked to your GitHub project repository.

"open_source_license":
~~~~~~~~~~~~~~~~~~~~~~

[
    1. MIT License,
    2. BSD license,
    3. ISC license,
    4. Apache Software License 2.0,
    5. GNU General Public License v3,
    6. Not open source
]

Let people know about this project license arrangements.

.. _Pyup.io: https://github.com/pyupio/pyup
.. _Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
.. _Django Settings: https://docs.djangoproject.com/en/3.2/ref/settings/
.. _Diátaxis:  https://junction-box.readthedocs.io/en/latest/Document-Framework/diataxis-intro.html