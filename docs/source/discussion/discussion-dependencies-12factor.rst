.. highlight:: rst
.. index:: dependency-discussion ; Index

.. _dependency-discussion:
=================================
Django Requirements Best Practice
=================================

Two minutes read.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::

  In this discussion, dependencies and requirements mean the same thing and are
  interchangeable.  In Python, by convention, dependencies are stored in a
  requirements.txt file.

  Documentation dependencies are outside the scope of this discussion.


Although there are many ways to configure the Django requirements file
structure, there is a commonality in many experienced developers'
approaches or preferred guidelines.

#. Version control dependencies.
#. Follow The 12 Factor App [#]_ principles of storing Dependencies.
#. Do not repeat yourself.

The 12 Factor guideline focus of this discussion is number two, Dependencies.

By following this guideline, we ensure strict separation between environment
dependencies.

Extract from 12 Factor Dependencies: [#]_
------------------------------------

*A twelve-factor app never relies on the implicit existence of system-wide
packages.*

*It declares all dependencies, completely and precisely, via a dependency
declaration manifest.*

*Furthermore, it uses a dependency isolation tool during execution to
ensure no implicit dependencies "leak in" from the surrounding system.*

*The full and explicit dependency specification is applied uniformly to both
production and development.*

Dependency Files Structure
--------------------------

From the outset, having a suitable dependency file structure has many
benefits as the project grows. Some key benefits are:

#. It simplifies the setup for developers new to the app.
#. Separation of concerns; see file structure below.
#. The requirements files are DRY [#]_.
#. Eliminate adding unrecorded dependencies to a virtual environment on a
   local machine.
#. Eliminate errors with local dev dependencies leaking and breaking production.
#. The requirements file size is smaller and more manageable.

.. _requirements-discussion:
Django Requirements Files
=========================

Following the same logic applied to our :ref:`settings<settings-discussion>`
configuration, our virtual/operating environments should have separate
requirements.txt files.

Each environment has different dependencies; for example, we would not run
django-debug-toolbar  [#]_ in production.

Our requirements file structure mirrors the settings file structure.

.. code-block:: python
   :caption: **Requirements File Structure**

   config
     └── requirements
          ├── base.txt
          ├── local.txt
          ├── production.txt
          ├── staging.txt
          └── test.txt


Why did we put requirements into the config folder?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While this arrangement is not required for a 12 Factor App [1]_, from a
logical perspective, we use dependency/requirements files as configuration
settings for our virtual/operating environments.

For that reason, we have chosen to group dependencies under the `config` folder.


requirements_dev.txt keeps it simple
-------------------------------------

Splitting all the dependencies into separate operating environments can add
some complexity to, for example,  setting up a local environment with the
ability to test.

The requirements_dev.txt reduces complexity for developers. Here, dependency
imports from local and test environments keep it simple for most developer
use cases.

.. literalinclude:: ../../../requirements_dev.txt
   :language: bash
   :caption: **requirements-dev.txt**

.. rubric:: Footnotes

.. [#] https://12factor.net/
.. [#] https://12factor.net/dependencies
.. [#] **D** o not **R** epeat **Y** ourself
.. [#] https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
