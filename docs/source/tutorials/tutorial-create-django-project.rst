.. highlight:: rst
.. index:: cookie-create-pkg ; Index


.. _cookie-create-pkg:
============================
Create a Django Cookiecutter
============================


|

See a list of the steps below to get up get your Django Cookiecutter Project up
and running fast.

.. note::

    This method allows you to create many django-cookiecutter projects without
    the need to re-create the virtual environments.

    For example, a new user may want to generate several projects trying
    different options.

    More advanced users may choose a different way to structure their virtual
    environments.
|

Pre-requisites
==============

`Python 3.6 <https://www.python.org/downloads/>`_ or greater installed on
your computer.

:ref:`Create a GitHub repository.<create-GH-repo>`


.. _create-cookiecutter-tutorial:
Tutorial
========

Navigate to the folder you wish to create your django-cookiecutter.

Here we are using `projects`.

.. code-block:: bash

    dev@aps1:~/projects$


.. _create-virtual-environemnt:
Create a Virtual Environment
----------------------------

Select the tab for your preferred Operating System.

.. note::

    The commands to create a virtual environment below will use the default
    Python version in your Operating System.

    If you prefer another python version installed on your computer, you can
    replace `python3` with `python3.n`, where n is the version number.

.. tab:: Linux

    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv my_venv

    You will have a folder structure similar to this.

    .. code-block:: bash

            projects
            └── my_venv


.. tab:: macOS


    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv my_venv

    You will have a folder structure similar to this.

    .. code-block:: bash

            projects
            └── my_venv

.. tab:: Windows

    If you have installed Python in your PATH and PATHEXT.

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        python3 -m venv my_venv

    Otherwise use

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        c:\>c:\Python36\python -m venv c:\path\to\projects\my_env

    You will have a folder structure similar to this.

    .. code-block:: cmd

            projects
            └── my_venv

.. _activate-virtual-environemnt:
Activate Virtual Environment
----------------------------

Ensure you are in the same folder as `my_env`. In this example, we are in the
`projects` folder.  Use the following command for your Operating System to
activate the virtual environment.

.. tab:: Linux

    .. code-block:: bash
        :caption: **bash/zsh**

        source my_env/bin/activate

.. tab:: macOS

    .. code-block:: bash
        :caption: **bash/zsh**

        source my_env/bin/activate


.. tab:: Windows

    .. code-block:: bash
            :caption: **cmd**

            my_env\Scripts\activate.bat

    .. code-block:: bash
            :caption: **PowerShell**

            my_env\Scripts\Activate.ps1


After activating the virtual environment, your cli will look something like
this, identifying the name of the virtual environment at the start.


.. code-block:: bash

    (my_env) dev@aps1:~/projects$


.. _install-cookiecutter:
Install Cookiecutter
--------------------

Firstly it's advisable to upgrade pip using the following command.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    pip install --upgrade pip

You will see something like this in your CLI.

.. code-block:: cmd

    Requirement already satisfied: pip in ./my_env/lib/python3.9/site-packages (21.2.3)
    Collecting pip
     Using cached pip-21.2.4-py3-none-any.whl (1.6 MB)
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 21.2.3
        Uninstalling pip-21.2.3:
          Successfully uninstalled pip-21.2.3
    Successfully installed pip-21.2.4

Install cookiecutter_ into your virtual environment.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    pip install cookiecutter


You will see something like this in your CLI.

.. code-block:: cmd

    Collecting cookiecutter
      Using cached cookiecutter-1.7.3-py2.py3-none-any.whl (34 kB)
    Collecting jinja2-time>=0.2.0
      Using cached jinja2_time-0.2.0-py2.py3-none-any.whl (6.4 kB)
    Collecting python-slugify>=4.0.0
      Using cached python_slugify-5.0.2-py2.py3-none-any.whl (6.7 kB)
    Collecting binaryornot>=0.4.4
      Using cached binaryornot-0.4.4-py2.py3-none-any.whl (9.0 kB)
    Collecting requests>=2.23.0
      Using cached requests-2.26.0-py2.py3-none-any.whl (62 kB)
    Collecting poyo>=0.5.0
      Using cached poyo-0.5.0-py2.py3-none-any.whl (10 kB)
    Collecting six>=1.10
      Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
    Collecting click>=7.0
      Using cached click-8.0.1-py3-none-any.whl (97 kB)
    Collecting Jinja2<4.0.0,>=2.7
      Using cached Jinja2-3.0.1-py3-none-any.whl (133 kB)
    Collecting chardet>=3.0.2
      Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
    Collecting MarkupSafe>=2.0
      Using cached MarkupSafe-2.0.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_
      x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (30 kB)
    Collecting arrow
      Using cached arrow-1.1.1-py3-none-any.whl (60 kB)
    Collecting text-unidecode>=1.3
      Using cached text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
    Collecting idna<4,>=2.5
      Using cached idna-3.2-py3-none-any.whl (59 kB)
    Collecting charset-normalizer~=2.0.0
      Using cached charset_normalizer-2.0.6-py3-none-any.whl (37 kB)
    Collecting certifi>=2017.4.17
      Using cached certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
    Collecting urllib3<1.27,>=1.21.1
      Using cached urllib3-1.26.7-py2.py3-none-any.whl (138 kB)
    Collecting python-dateutil>=2.7.0
      Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
    Installing collected packages: six, python-dateutil, MarkupSafe, urllib3,
     text-unidecode, Jinja2, idna, charset-normalizer, chardet, certifi, arrow,
     requests, python-slugify, poyo, jinja2-time, click, binaryornot, cookiecutter
    Successfully installed Jinja2-3.0.1 MarkupSafe-2.0.1 arrow-1.1.1
     binaryornot-0.4.4 certifi-2021.5.30 chardet-4.0.0 charset-normalizer-2.0.6
     click-8.0.1 cookiecutter-1.7.3 idna-3.2 jinja2-time-0.2.0 poyo-0.5.0
     python-dateutil-2.8.2 python-slugify-5.0.2 requests-2.26.0 six-1.16.0
     text-unidecode-1.3 urllib3-1.26.7


Check new packages installed into your virtual environment.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    pip freeze

You will see something like this in your CLI.

.. code-block:: cmd

    arrow==1.1.1
    binaryornot==0.4.4
    certifi==2021.5.30
    chardet==4.0.0
    charset-normalizer==2.0.6
    click==8.0.1
    cookiecutter==1.7.3
    idna==3.2
    Jinja2==3.0.1
    jinja2-time==0.2.0
    MarkupSafe==2.0.1
    poyo==0.5.0
    python-dateutil==2.8.2
    python-slugify==5.0.2
    requests==2.26.0
    six==1.16.0
    text-unidecode==1.3
    urllib3==1.26.7

.. _create_django-project:
Create Your Django Project
--------------------------

In your projects folder, use the following command.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    cookiecutter https://github.com/imAsparky/django-cookiecutter

Cookiecutter will ask questions to set your package up.
If you're unsure or don't know what to enter, stick with the defaults.

See :ref:`Reference-Inputs<project-inputs>` for more details about the
django-cookiecutter project options.

.. _an-example-django:
An Example Django Project
-------------------------

.. code-block:: cmd
    :caption: **An example package created with some non default selections**

      (my_env) dev@aps1:~/projects$cookiecutter
      https://github.com/imAsparky/django-cookiecutter
      author_name [Mark Sevelj]:
      email [mark@example.com]: mark@example.com
      github_username [imAsparky]:
      github_user_email [mark@example.com]:
      project_name [Django Boilerplate]: My New Django
      git_project_name [my-new-django]:
      project_slug [my_new_django]:
      project_short_description [A Django project with all the boilerplate]: An example Django Project for django-cookiecutter
      version [0.1.0]:
      Select create_conventional_commits_edit_message:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select use_GH_custom_issue_templates:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select automatic_set_up_git_and_initial_commit:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select use_pre_commit:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select create_repo_auto_test_workflow:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select use_GH_action_semantic_version:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select include_sphinx_docs:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select use_readthedocs:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select include_documentation_templates:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select include_how_to_contribute_template:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select include_contributor_covenant_code_of_conduct:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      ALLOWED_HOSTS [www.example.com]:
      DEBUG [False]:
      INTERNAL_IPS [127.0.0.1]:
      LANGUAGE_CODE [en-au]:
      LANGUAGES [hi]:
      TIME_ZONE [UTC]:
      USE_L10N [True]:
      USE_I18N [True]:
      SITE_ID [1]:
      Select use_django_allauth:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select use_repo_status_badge:
      1 - no
      2 - concept
      3 - wip
      4 - active
      Choose from 1, 2, 3, 4 [1]: 2  (NON DEFAULT)
      Select use_pyup_io:
      1 - y
      2 - n
      Choose from 1, 2 [1]:
      Select open_source_license:
      1 - MIT license
      2 - BSD license
      3 - ISC license
      4 - Apache Software License 2.0
      5 - GNU General Public License v3
      6 - Not open source
      Choose from 1, 2, 3, 4, 5, 6 [1]: 2  (NON DEFAULT)
      (my_env) dev@aps1:~/projects$

.. hint::

  See below, notice the project_name format and how django-cookiecutter
  automatically formats the name for your GitHub repository and python module
  as default inputs.

  .. code-block:: cmd

    project_name [Django Boilerplate]: My New Django
    git_project_name [my-new-django]:
    project_slug [my_new_django]:


.. new-folder-structure::
Folder Structure
----------------

If you have been following along the Tutorial order, your directory structure
will look something like this.

.. code-block:: cmd

  projects
    ├── my-new-django
    │   ├── .git
    │   ├── .github
    │   ├── .pre-commit-config.yaml
    │   ├── .pyup.yml
    │   ├── .readthedocs.yaml
    │   ├── CHANGELOG.md
    │   ├── LICENSE.rst
    │   ├── pytest.ini
    │   ├── README.rst
    │   ├── my_new_django
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   │
    │   ├── docs
    │   ├── tox.ini
    │   ├── manage.py
    │   └── requirements_dev.txt
    │
    └── my_env
        ├── bin
        ├── include
        ├── lib
        ├── lib64 -> lib
        └── pyvenv.cfg


.. include:: tutorial-segment-create-env-variable.rst

Test Your Project
-----------------

.. code-block:: bash

    python3 manage.py runserver


Congratulations, you have created your new Django project.


Whats next?
-----------

:ref:`Create your first git push<create-first-git-push>`.

or you can

Check out our other :ref:`Tutorials<tutorial-index>` for more information on
how to get the most out of your cookiecutter package.



.. _cookiecutter: https://cookiecutter.readthedocs.io/en/1.7.2/installation.html
