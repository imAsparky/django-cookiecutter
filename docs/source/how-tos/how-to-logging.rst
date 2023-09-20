.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-logging ; Index

.. _how-to-logging:

==============
Logging Config
==============

You can modify the logging configuration through `.env`` settings files.

All environments share the same logging file ENV Variable Name with a prefix.
For example `DJANGO_LOGGING_LEVEL` for the local environment would be
`LOCAL_DJANGO_LOGGING_LEVEL`

Sharing a common ENV Variable Name with a prefix allows greater control over logging.


Rotating Log Files
------------------

django-cookiecutter uses Rotating Logs to prevent log file size from growing
too large.  The default settings, see below, are located in
`config/settings/base.py`.

The `backupCount` setting allows up to five log files before it starts removing them.

The `maxBytes` setting is the maximum size a file can be before it is closed and rotated to a new file.

.. code-block:: python
    :linenos:
    :emphasize-lines: 8,9

    "rotated_logs": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": DJANGO_LOG_FILE,
        "level": DJANGO_LOGGING_LEVEL,
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "backupCount": 5,
        "maxBytes": 10485760,
    },


Local
-----

See the local environment configuration file below.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 3

     my-django-project
         └── .env
             ├── .local
             ├── .production
             ├── .staging
             └── .testing


.. code-block:: bash
    :linenos:
    :emphasize-lines: 11, 12, 13

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




Staging and Production
----------------------

`Staging` and `Production` environments add the environment prefix to the
ENV Variable to differentiate between the two environments.

See the production file below, showing the addition of the `_PRODUCTION`
suffix, and specifying the production logging file location.


.. code-block:: bash
    :linenos:
    :emphasize-lines: 5

     my-django-project
         └── .env
             ├── .local
             ├── .production
             ├── .staging
             └── .testing


.. code-block:: bash
    :linenos:
    :emphasize-lines: 9, 10, 11

    # Production Environment ENV Keys

    # Production Environment Django
    PROD_ALLOWED_HOSTS=''
    PROD_DATABASE_URL=''
    PROD_DB_API_KEY=''
    PROD_DJANGO_DEBUG=False
    PROD_DJANGO_INTERNAL_IPS=[]
    PROD_DJANGO_LOG_FILE='logging/rotating.log'
    PROD_DJANGO_LOGGING_LEVEL='INFO'
    PROD_DJANGO_LOGGING_MAIL_ADMINS='ERROR'
    # For the docker image
    PROD_DJANGO_MANAGEPY_MIGRATE=on
    PROD_DJANGO_SECRET_KEY=='!!!INSECURE_PRODUCTION_SECRET!!!'
    PROD_DJANGO_SETTINGS_MODULE='config.settings.production'
    PROD_DJANGO_TEMPLATES_CSS=''
    PROD_MEDIA_URL='media-'
    PROD_STATIC_URL='static/'
    # static options are local or S3
    PROD_USE_STATIC='S3'
    PROD_TAILWIND_CSS_DEV=False

    # Production Environment S3 access
    PROD_AWS_ACCESS_KEY_ID=''
    # If using the default leave ENDPOINT_URL unset
    PROD_AWS_S3_ENDPOINT_URL=''
    # If using the default leave AWS_LOCATION unset
    PROD_AWS_LOCATION=''
    PROD_AWS_SECRET_ACCESS_KEY=''
    PROD_AWS_S3_REGION_NAME=''
    PROD_AWS_S3_OBJECT_PARAMETERS=''
    PROD_AWS_STORAGE_BUCKET_NAME=''

    # Production Environment Email Settings
    PROD_EMAIL_BACKEND=''
    PROD_EMAIL_HOST=''
    PROD_EMAIL_PORT=''
    PROD_EMAIL_HOST_USER=''
    PROD_EMAIL_HOST_PASSWORD=''
    PROD_EMAIL_USE_TLS=''



Email Admins
------------

By default, Sending emails to admins is set to `ERROR` for all environments.

You can change what logging level the Admins will receive an email with the
email admins variable; see production settings file extract below.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 3

    PROD_DJANGO_LOG_FILE='logging/rotating.log'
    PROD_DJANGO_LOGGING_LEVEL='INFO'
    PROD_DJANGO_LOGGING_MAIL_ADMINS='ERROR'
