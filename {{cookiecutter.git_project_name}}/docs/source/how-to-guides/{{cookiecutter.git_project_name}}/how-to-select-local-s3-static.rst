.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-static-local-s3 ; Index


.. _how-to-static-local-s3:

=======================
Static: Dev S3 or Local
=======================

{{ cookiecutter.project_name }} uses Digital Ocean S3 (Simple Storage Service) storage for static and
media files.


Overview
========

Its faster-developing CSS, Media files and other Static Assets when using local
storage.

{{ cookiecutter.project_name }} provides the means in `config/settings/local.py` to select which
Storage to use with an `Environment Variable`.


.. code-block:: python
    :caption: **config/settings/local.py**

    USE_STATIC = env("USE_STATIC", default="Local")

    # Digital Ocean S3 Storage Configuration

    if USE_STATIC == "S3":

        AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="AWS_KEY_NOT_SET")
        AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="AWS_SECRET_NOT_SET")

        ...

.. note::

    1. Changing the `USE_STATIC` variable requires restarting the local server for
       the new setting to take effect.

    2. The environment variable can be set using the .env/.local file or by setting
       the environment variable, see below for descriptions.

    3. `./manage.py collectstatic` should be run after changing the `USE_STATIC`
       value so the latest static files are available.

|

.. _how-to-select-storage-manual:

Manual: Select Storage
======================


1. .env file
------------

Using the `.env/.local` file set `LOCAL_USE_STATIC` to Local or S3.

.. code-block:: console
    :caption: .env/.local
    :linenos:
    :emphasize-lines: 16

    # Local Environment ENV Keys

    # Local Environment Django
    LOCAL_ALLOWED_HOSTS=localhost,0.0.0.0,127.0.0.1,testserver
    # Local database options: sqlite3, other.
    # If using other, a LOCAL_DATABASE_URL connection string must be supplied.
    LOCAL_DJANGO_DATABASE=sqlite3
    LOCAL_DATABASE_URL=""
    LOCAL_DJANGO_DEBUG=True
    LOCAL_DJANGO_INTERNAL_IPS=127.0.0.1,10.0.2.2
    LOCAL_DJANGO_LOG_FILE='logging/rotating.log'
    LOCAL_DJANGO_LOGGING_LEVEL='DEBUG'
    LOCAL_DJANGO_LOGGING_MAIL_ADMINS='ERROR'
    # For the docker image
    LOCAL_DJANGO_MANAGEPY_MIGRATE=on
    LOCAL_DJANGO_SECRET_KEY='!!!DODGY_LOCAL_SECRET!!!'
    LOCAL_DJANGO_SETTINGS_MODULE='config.settings.local'
    LOCAL_DJANGO_TEMPLATES_CSS="/static/css/styles.css"
    LOCAL_MEDIA_URL='media-lo/'
    LOCAL_STATIC_URL='static-lo/'
    # static options are Local or S3
    LOCAL_USE_STATIC='Local'
    LOCAL_TAILWIND_CSS_DEV=True

    # Local Environment S3 access
    LOCAL_AWS_ACCESS_KEY_ID=""
    # If using the default leave ENDPOINT_URL unset
    LOCAL_AWS_S3_ENDPOINT_URL=""
    # If using the default leave AWS_LOCATION unset
    LOCAL_AWS_LOCATION=""
    LOCAL_AWS_SECRET_ACCESS_KEY=""
    LOCAL_AWS_S3_REGION_NAME=""
    LOCAL_AWS_S3_OBJECT_PARAMETERS=""
    LOCAL_AWS_STORAGE_BUCKET_NAME=""

    # Local Environment Email Settings
    LOCAL_EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
    LOCAL_EMAIL_HOST=""
    LOCAL_EMAIL_PORT=""
    LOCAL_EMAIL_HOST_USER=""
    LOCAL_EMAIL_HOST_PASSWORD=""
    LOCAL_EMAIL_USE_TLS=""


|

2. Environment Variable
-----------------------

Set Environment variables.

.. code-block:: bash
    :caption: Set the Environment Variable for Local

    export LOCAL_USE_STATIC="Local"

|

.. code-block:: bash
    :caption: Set the Environment Variable for S3

    export LOCAL_USE_STATIC="S3"

|

.. code-block:: bash
    :caption: Unset the Environment Variable

    unset LOCAL_USE_STATIC

|


.. _how-to-select-storage-bash:

Bash: Select Storage
====================

Simplify storage selection using Bash aliases.



Add these lines in `~/.bashrc` or, if it exists `.bash_aliases`.

.. note::

    If `mpcs` exists, replace with the `mpcs` alias below or unexpected
    behaviour may occur.

    These `aliases` unset the environment variable after Collectstatic has run.


.. code-block:: console


    # manage.py commands
    alias mpcs='export LOCAL_USE_STATIC="Local" && python3 manage.py collectstatic --noinput && unset LOCAL_LOCAL_USE_STATIC'
    alias mpcs3='export LOCAL_USE_STATIC="S3" && python3 manage.py collectstatic --noinput && unset LOCAL_LOCAL_USE_STATIC'

|

.. _how-to-document-storage-bash:

Bash: Document Storage
======================

Selecting Local or S3 storage for documentation development using `bash aliases`.

Add or replace existing bash aliases with the ones below.


.. code:: console

    # sphinx build
    alias sbl='sphinx-build -b html docs/source docs/html && export LOCAL_USE_STATIC="Local" && python3 manage.py collectstatic --noinput && unset LOCAL_USE_STATIC'
    alias sbs3='sphinx-build -b html docs/source docs/html && export LOCAL_USE_STATIC="S3" && python3 manage.py collectstatic --noinput && unset LOCAL_USE_STATIC'



.. note::

    After saving the file with new aliases, close and re-open your bash
    terminal to make them available.
