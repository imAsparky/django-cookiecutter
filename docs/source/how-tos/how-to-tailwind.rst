.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-tail ; Index

.. _how-to-tail:

=========================
Tailwind & Browser Reload
=========================

.. warning::

    django-tailwind requires Node js installed on your development machine.

    **If you don't have Node.js installed on your machine,** please follow
    installation instructions from the official `Node.js page` [#]_.



django-tailwind employs django-browser-reload to provide a smooth development
experience styling Django projects with TailwindCss

See `django-tailwind` [#]_, `django-browser-reload` [#]_ and `tailwindcss` [#]_
for detailed information about using these tools.


django-browser-reload
---------------------


django-tailwind handles all the configuration for django-browser-reload.


django-tailwind
---------------


.. _how-to-tail-get-started:
Getting Started
~~~~~~~~~~~~~~~

Once you have created your django-cookiecutter project, you must install
django-tailwind dependencies.

From the CLI in your virtual environment, type the command

.. code-block:: bash

	python3 manage.py tailwind install


Running the Server
~~~~~~~~~~~~~~~~~~

When developing your web page and its styling, django-tailwind uses
django-browser-reload to update all changes as you save them.

To start the live reload server, from the CLI, type the command.

.. code-block:: bash

	python3 manage.py tailwind start


Open another terminal and activate your virtual environment; from the CLI,
type the command.

.. code-block:: bash

	python3 manage.py runserver

Build CSS File
~~~~~~~~~~~~~~

To build a production-ready CSS file and save it in your static folder,
from the CLI, type the commands.

.. code-block:: bash

	python3 manage.py tailwind build

.. code-block:: bash

    python3 manage.py collectstatic


Troubleshooting
~~~~~~~~~~~~~~~

*An extract from django-tailwind docs.*


Tailwind CSS requires Node.js to be installed on your machine.
Node.js is a JavaScript runtime that allows you to run JavaScript code outside
the browser.  Most (if not all) of the current frontend tools depend on Node.js.

Sometimes (especially on Windows), the Python executable cannot find the
npm binary installed on your system.  In this case, you need to set the path
to the npm executable in the settings.py file manually.

.. tab:: Linux/Mac

    .. code-block:: bash

        NPM_BIN_PATH = '/usr/local/bin/npm'


.. tab:: Windows

    On Windows it might look like this:

    .. code-block:: cmd

        NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

.. note::

    Please note that the path to the npm executable may be different for your
    system.

    To get the npm path, try running the command `which npm` in your terminal.

|

.. rubric:: Footnotes

.. [#] https://nodejs.org/en/
.. [#] https://github.com/timonweb/django-tailwind
.. [#] https://github.com/adamchainz/django-browser-reload
.. [#] https://tailwindcss.com/docs
