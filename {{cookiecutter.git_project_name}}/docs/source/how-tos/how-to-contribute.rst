.. highlight:: rst
.. index:: contribute-how-to ; Index

.. _contribute-how-to:
====================
Contributing How-to
====================

**4 minute read.**

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Contributions are very welcome and appreciated!

You can contribute in many ways.

Please take a moment to read our :ref:`code of conduct<code-of-conduct>` for
how we would like the community to treat each other.

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report a bug_!

A `Bug Issue Template` is available to assist you
provide all the necessary information.

.. _bug: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.git_project_name}}/issues

Fix Bugs
~~~~~~~~

Look through {{cookiecutter.project_name}} GitHub issues_ for bugs.

Anything labelled with **'bug'** and **'help wanted'** is open to anyone
wishing to assist.


Implement Features
~~~~~~~~~~~~~~~~~~

Look through {{cookiecutter.project_name}} GitHub issues_ for features.

Anything labelled with **'enhancement'** and **'help wanted'** is open to
anyone wishing to assist.


Write Documentation
~~~~~~~~~~~~~~~~~~~

{{cookiecutter.project_name}} strives to have excellent documentation for several reasons:

#. Excellent documentation improves the user's experience.
#. Excellent documentation helps when reviewing old features or code.

At the core of that effort is following the Diátaxis Framework and
documentation philosophy.

{{cookiecutter.project_name}} provides the four pillars Tutorials, How-to, Reference and
Discussion with templates to make writing documentation easy.

Take a look at :ref:`our growing list of templates <index-template>` here.

Here is a TLDR of the documentations structure:

1. Tutorial:

   a. Allow the learner to understand what goals they will achieve before
      they start.
   b. A tutorial helps a beginner achieve basic competence.
   c. Allow the user to learn by doing.
   d. Get the learner productive and succeeding from the very start.

2. How-to:

   a. How-to guides are goal-oriented directions, much like a recipe.
   b. The goal of a how-to is to solve a problem or complete an unfamiliar task.
   c. Explanations aren't necessary when following a how-to guide.
   d. How-to guides should be flexible and adaptable to many use cases.

3. Reference:

   a. References are technical descriptions of the machinery and how to
      operate it.
   b. A reference guides focus is the product and must describe it as
      succinctly as possible.
   c. Users consult reference material, so it should not contain any ambiguity.

4. Discussions:

   a. Discussions clarify and illuminate a particular topic.
   b. Discussions are understanding-oriented.
   c. Discussions deepen and broaden the reader's understanding of a subject.
   d. Connections, even to things outside the immediate topic, can add clarity
      and context.

See this `Diátaxis summary <https://junction-box.readthedocs.io/en/latest/
Document-Framework/index-document-framework.html>`_  for more information to
help you write better documentation.

Docstrings
~~~~~~~~~~

{{cookiecutter.project_name}} uses Sphinx to document the API.  Class's, modules, or
functions must have at least a single line docstring, ending in a period to
pass code quality checks.

The docstring should convey `what` is done, not `how` it is done to your
users for clarity and consistency.

See the `amazing_new_feature.py` example below.

.. code-block:: python
    :linenos:

    """Classes for adding Amazing New Features."""

    class AmazingNewFeaturesFromOld:
        """A class of making old features new again."""

        def amazing_new_feature_from_old_1(self):
            """Take some old feature and make it fresh again."""

        def amazing_new_feature_from_old_2(self):
            """Take another old feature and make it fresher."""

    class AmazingNewFeatures:
        """A class of making brand new features."""

        def amazing_new_feature_1(self):
            """Improve user experience feature one."""

        def amazing_new_feature_2(self):
            """Improve user experience feature two."""


Submit Feedback
~~~~~~~~~~~~~~~

The best way to provide feedback is to file
an `Issue <https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.git_project_name}}/issues>`_.

A selection of templates is available to help you get your message across.

* This is a volunteer-driven project, and all contributions are welcome :)

Get Started
-----------

Ready to contribute?

Here's how to set up `{{cookiecutter.git_project_name}}` for local development. We have
demonstrated this is going into a local `projects` folder.

1. Create a virtual environment.

.. note::

    The commands to create a virtual environment below will use the default
    Python version in your Operating System.

    If you prefer another python version installed on your computer, you can
    replace `python3` with `python3.n`, where n is the version number.

.. important::

    If you are writing documentation and using a preview function in your
    IDE then the minimum version for documentation is Python3.9, and it is
    also recommended to pip install:

    | furo==2021.8.17b43
    | myst-parser==0.15.1
    | Sphinx==4.1.2
    | sphinx-copybutton==0.4.0
    | sphinx_inline_tabs==2021.4.11b9


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

2. From your GitHub account, fork the `{{cookiecutter.git_project_name}}` repository.


3. In your projects folder, clone your fork locally, install the developer
   requirements and set the local git commit message template.

.. code-block:: bash

    git clone git@github.com:your_git_user_name_here/django-cookiecutter.git

    cd django-cookiecutter

    git config --local commit.template .github/.git-commit-template.txt

    pip install -r requirements_dev.txt

You will have a folder structure similar to this.

.. code-block:: bash

        projects
         ├── venv
         └── django-cookiecutter

4. Create a branch for local development.

.. code-block:: bash

    git checkout -b issue-nn  # Convention is to use issue number.

    git checkout -b name-of-your-bugfix-or-feature # Altenative to the convention.


Now you can make your changes locally.

5. When you're changes with tests and documentation are complete, run
   pre-commit and tox.

.. code-block:: bash

    git add .
    pre-commit
    tox

6. After successful pre-commit and tox, commit your changes and push your
   branch to GitHub.

.. note::

    {{cookiecutter.project_name}} uses python-semantic-release.

    For semantic version to work, commit messages must follow
    `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.

    See an example of how they look
    `here <https://github.com/imAsparky/django-cookiecutter>`_.

    If you have followed the contributing guidelines to this point, the local
    commit message template has help built-in.

.. code-block:: bash

    git commit
    git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, please check that it meets these guidelines:

1. The pull request changes must be covered with tests.
2. If the pull request adds functionality, you should add the functionality to the documentation.

   Documentation :ref:`templates <index-template>` are provided to assist you.
3. Your changes must include a docstring to pass code quality checks.
4. Please run pre-commit and Tox locally before making a pull request.


**If you have gotten this far, thank you for your time and contribution.**


.. _issues: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.git_project_name}}/issues
