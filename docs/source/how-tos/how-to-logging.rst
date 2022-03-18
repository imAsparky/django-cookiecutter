.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-logging ; Index

.. _how-to-logging:

==============
Logging Config
==============

You can modify the logging configuration through `.env`` settings files.

All environments share the same logging file ENV Variable Name.

Sharing a common ENV Variable Name keeps configuration simplifies changing the
logging file name for each environment.


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


Local and Test
--------------

`Local` and `Test` environments also share the same logging level ENV Variable name.

See the local environment configuration file below.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 3,6

     my-django-project
         └── .env
             ├── .local
             ├── .production
             ├── .staging
             └── .testing

.. code-block:: bash
    :linenos:
    :emphasize-lines: 3, 4

    ALLOWED_HOSTS=localhost,0.0.0.0,127.0.0.1
    DJANGO_DEBUG=True
    DJANGO_LOG_FILE="logging/rotating_local.log"
    DJANGO_LOGGING_LEVEL="DEBUG"
    DJANGO_LOGGING_MAIL_ADMINS="ERROR"
    DJANGO_MANAGEPY_MIGRATE=on
    DJANGO_SECRET_KEY="!!!INSECURE_PRODUCTION_SECRET!!!"
    DJANGO_SETTINGS_MODULE=config.settings.local
    EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
    INTERNAL_IPS=127.0.0.1,10.0.2.2
    DB_ENGINE=""
    DB_NAME=""
    DB_USER=""
    DB_PASSWORD=""
    DB_HOST=""
    DB_PORT=""



Staging and Production
----------------------

`Staging` and `Production` environments add the environment suffix to the
ENV Variable to differentiate between the two environments.

See the production file below, showing the addition of the `_PRODUCTION`
suffix, and specifying the production logging file location.


.. code-block:: bash
    :linenos:
    :emphasize-lines: 4, 5

     my-django-project
         └── .env
             ├── .local
             ├── .production
             ├── .staging
             └── .testing


.. code-block:: bash
    :linenos:
    :emphasize-lines: 2,3

    DJANGO_DEBUG=FALSE
    DJANGO_LOG_FILE="logging/rotating_production.log"
    DJANGO_LOGGING_LEVEL_PRODUCTION="INFO"
    DJANGO_LOGGING_MAIL_ADMINS="ERROR"
    DJANGO_MANAGEPY_MIGRATE=on
    DJANGO_SECRET_KEY=""
    DJANGO_SETTINGS_MODULE=config.settings.production
    DB_ENGINE=""
    DB_NAME=""
    DB_USER=""
    DB_PASSWORD=""
    DB_HOST=""
    DB_PORT=""
    INTERNAL_IPS=""


Email Admins
------------

By default, Sending emails to admins is set to `ERROR` for all environments.

You can change what logging level the Admins will receive an email with the
email admins variable; see below.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 4

    DJANGO_DEBUG=FALSE
    DJANGO_LOG_FILE="logging/rotating_production.log"
    DJANGO_LOGGING_LEVEL_PRODUCTION="INFO"
    DJANGO_LOGGING_MAIL_ADMINS="ERROR"
    DJANGO_MANAGEPY_MIGRATE=on
    DJANGO_SECRET_KEY=""
    DJANGO_SETTINGS_MODULE=config.settings.production
    DB_ENGINE=""
    DB_NAME=""
    DB_USER=""
    DB_PASSWORD=""
    DB_HOST=""
    DB_PORT=""
    INTERNAL_IPS=""
