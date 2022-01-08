.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-quickstart ; Index

.. _how-to-quickstart:
==========
Quickstart
==========

See :ref:`Reference Project Inputs<project-inputs>` for all information
collected to create a new django-cookiecutter project.

Create a GitHub Repository
--------------------------

Your new GitHub repository information is required to generate
your django-cookiecutter in these steps.

project_name
~~~~~~~~~~~~

The name of your new Django project,  used in the documentation,
so spaces and any characters are acceptable here.

Typically the repository name in sentence form.

project_short_description
~~~~~~~~~~~~~~~~~~~~~~~~~

A  sentence describes your Django project.

Typically the repository description.


Create Virtual Environment
--------------------------

**Select the tab for your preferred Operating System.**

.. tab:: Linux

    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv venv
        source venv/bin/acivate
        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            projects
            └── venv


.. tab:: macOS


    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv venv
        source venv/bin/acivate
        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            projects
            └── venv

.. tab:: Windows

    If you have installed Python in your PATH and PATHEXT.

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        python3 -m venv venv

        C:\> venv\Scripts\activate.bat  # cmd.exe
        PS C:\> venv\Scripts\Activate.ps1 # Powershell

        pip install --upgrade pip

    Otherwise use

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        c:\>c:\Python36\python -m venv c:\path\to\packages\my_env
        PS C:\> <venv>\Scripts\Activate.ps1

        C:\> venv\Scripts\activate.bat  # cmd.exe
        PS C:\> venv\Scripts\Activate.ps1 # Powershell

        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            projects
            └── venv

.. _quick_install-cookiecutter:
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

Start Django Cookiecutter
-------------------------

In your projects folder, use the following command.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    cookiecutter https://github.com/imAsparky/django-cookiecutter

Cookiecutter will ask questions to set your package up.
If you're unsure or don't know what to enter, stick with the defaults.

See :ref:`Reference-Inputs<project-inputs>` for more details about the
django-cookiecutter project options.

.. code-block:: bash

    projects
        ├── venv
        └── my-new-django


Install Dependencies
--------------------


Change into your project directory.


.. code-block:: bash

    cd <your django project folder>


Install dependencies.

.. code-block:: bash

    pip install -r requirements_dev.txt


.. include:: ../tutorials/tutorial-segment-create-env-variable.rst

Run Your Project
-----------------

.. code-block:: bash

    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver

In your browser navigate to 127.0.0.1/admin

Congratulations, you have created your new Django project.

Depending on your chosen options, there are several ways to proceed with
pushing to GitHub.  If you are unsure, see our
:ref:`git push tutorial<create-first-git-push>` for more information.


Default Testing Database
------------------------

By default, your Django project test DB is db.sqlite3.

See config/settings/test.py and .env/.testing.

.. code-block:: python
    :caption: **config/settings/test.py**

    ...

    # Selects which database to use for testing, default=sqlite3 .
    TESTING_DATABASE = env("TESTING_DATABASE")

    if TESTING_DATABASE == "sqlite3":

        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                # "NAME": BASE_DIR / "db.sqlite3",
            }
        }

    else:

        DATABASES = {"default": env.db()}


.. code-block:: text
    :caption: **.env/.testing**

    ...

    # Testing database options: sqlite3, other.
    # If using other, a DB_URL connection string must be supplied.
    TESTING_DATABASE=sqlite3
    DB_URL=""


To select another testing database, you can:

#.  Update .env/.testing variables with your preferences.
#.  Provide ENV vars with your preferences.

.. code-block:: text
    :caption: **Option 1**

    ...

    # Testing database options: sqlite3, other.
    # If using other, a DB_URL connection string must be supplied.
    TESTING_DATABASE=other  # Change to other.
    DB_URL=Your_connection_string_here

.. code-block:: bash
    :caption: **Option 2**

    export TESTING_DATABASE=other
    export DB_URL=Your_connection_string_here


.. _cookiecutter: https://cookiecutter.readthedocs.io/en/1.7.2/README.html
