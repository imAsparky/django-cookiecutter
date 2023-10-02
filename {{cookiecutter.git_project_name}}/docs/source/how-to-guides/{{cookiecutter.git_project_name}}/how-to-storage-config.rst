.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-storage-config ; Index


.. _how-to-storage-config:

=====================
Storage Configuration
=====================


{{ cookiecutter.project_name }} uses Digital Ocean S3 (Simple Storage Service) storage for static and
media files.  Digital Ocean uses `AWS S3 API`, so is compatible with django-storages.

Configuration for S3 storage is done in several places and for each operating
environment.

Overview
========

boto3 [#]_ is the interface Django uses to interact with S3 backends that
comply with Amazon Web Services S3 API.

django-storages [#]_ provides a nice api for boto3.  Digital Oceans S3 storage
is AWS S3 compatible; however it offers a reduced functionality set.

Definitions
-----------

How Django defines the following file types.

Media
~~~~~

Files uploaded and used by users.


Static
~~~~~~

Files uploaded and used by the website, e.g. CSS, javascript etc.


Storage Backend
===============


Below is an example from `config/storage/backends.py`.
Adding other storage classes is possible in this file.

.. code-block:: python
    :caption: **config/storage/backends.py**

    import environ
    from storages.backends.s3boto3 import S3Boto3Storage

    env = environ.FileAwareEnv()

    class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = env("STATIC_URL")
    default_acl = "public-read"
    file_overwrite = True



Configuration Settings
======================


django-storages require many environment variable settings located in several
different settings files.

.. note::

    All settings files exist in `config/settings/`, including a `base` file
    and four separate `environment` files.

|

Base Settings
-------------

The following settings in `base.py` are standard settings and values.

django-storages use these to extend storage from the filesystem to S3.

.. code-block:: python
    :caption: **config/settings/base.py**

    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

|

Environment Settings
--------------------

In addition to the `base` settings, there are four environment settings files,
local, testing, staging and production.  The settings for S3 are virtually
identical in each of these files, but they do offer the ability to use different
environment settings if the need arises.

|

Additional information for the settings, shown below, is available in
django-storages documentation.

The emphasised lines 34-47 are the settings most probably relevant to change.
For example, the defaults for `DEFAULT_FILE_STORAGE` (media files) and
`STATICFILES_STORAGE` (static files) demonstrate the chosen fallback
`storage` backend.

.. code-block:: python
    :caption: **config/settings/local.py**
    :linenos:
    :emphasize-lines: 34-47

    # `USE_STATIC` options are `Local` or `S3`
    USE_STATIC = env("LOCAL_USE_STATIC", default="Local")

    # Digital Ocean S3 Storage Configuration
    if USE_STATIC == "S3":
        AWS_ACCESS_KEY_ID = env(
            "LOCAL_AWS_ACCESS_KEY_ID",
            default="LOCAL_AWS_KEY_NOT_SET",
        )
        AWS_SECRET_ACCESS_KEY = env(
            "LOCAL_AWS_SECRET_ACCESS_KEY",
            default="LOCAL_AWS_SECRET_NOT_SET",
        )

        AWS_S3_REGION_NAME = env(
            "LOCAL_AWS_S3_REGION_NAME",
            default="syd1",
        )
        AWS_S3_ENDPOINT_URL = env(
            "LOCAL_AWS_S3_ENDPOINT_URL",
            default=f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )
        AWS_STORAGE_BUCKET_NAME = env(
            "LOCAL_AWS_STORAGE_BUCKET_NAME",
            default="tb-s3",
        )
        AWS_LOCATION = env(
            "LOCAL_AWS_LOCATION",
            default=f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com",
        )

        AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=1"}

        STORAGES = {
            "default": {
                "BACKEND": env(
                    "DEFAULT_FILE_STORAGE",
                    default="core.storage.backends.MediaRootS3Boto3Storage",
                )
            },
            "staticfiles": {
                "BACKEND": env(
                    "STATICFILES_STORAGE",
                    default="core.storage.backends.StaticRootS3Boto3Storage",
                )
            },
        }

        # Static url must end with default STATIC_URL from env var or base.py added to
        # S3 storage location.
        STATIC_URL = env("LOCAL_STATIC_URL", default="static-lo/")

        # Media url must end with default MEDIA_URL from env var or base.py added to
        # S3 storage location.
        MEDIA_URL = env("LOCAL_MEDIA_URL", default="media-lo/")

        # Set the url for the css file
        LOCAL_DJANGO_TEMPLATES_CSS = f"{STATIC_URL}css/styles.css"


|

.. rubric:: Footnote

.. [#] https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
.. [#] https://django-storages.readthedocs.io/en/latest/
