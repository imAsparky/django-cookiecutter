.. include:: ../extras.rst.txt
.. highlight:: rst
.. index:: BaseSoftLogS3Model-tutorial ; Index


.. _BaseSoftLogS3Model-tutorial:

==================
Models - SoftLogS3
==================

This tutorial will demonstrate.

#. Setting up an `BaseSoftLogS3Model` model.
#. Adding Optional feature models.

   #. `BaseAuditLog`.
   #. `BaseS3ImageModel`.
   #. `BaseS3FileModel`.

|

Pre-requisites
==============

|

A Django app is available to create the model.
An understanding of Django models.

|

1. Simple `BaseSoftLogS3Model`
==============================

|

1. In your `models.py` file import the Abstract Base Model.

.. code-block:: python
    :caption: `models.py`

    from core.models.base import BaseSoftLogS3Model

|

2. Create your new model, inheriting `BaseSoftLogS3Model`.
3. Override the `Meta` class `verbose_name` and `verbose_name_plural` with
   a name meaningful to you.

        These names are used in the `Admin panel` amongst other places.


.. code-block:: python
    :caption: `models.py`

    class MyNewModel(BaseSoftLogS3Model):

        class Meta:
            verbose_name = "My New Model"
            verbose_name_plural = "My New Models"

|

4. Add `fields` to your new model.

|

.. code-block:: python
    :caption: `models.py`

    class MyNewModel(BaseSoftLogS3Model):

        class Meta:
            verbose_name = "My New Model"
            verbose_name_plural = "My New Models"

        # Your custom field names
        field_1 = models.CharField(
                max_length=255,
                blank=False,
                null=False,
            )
        field_2 = models.TextField(
                max_length=1000,
                blank=True,
                null=True,
            )

|

Optional Feature Models
=======================

|


After creating the `BaseSoftLogS3Model` you can add new functionality with Optional Feature Models.

|


Audit Log
---------

|

1. In your `models.py` file import the Abstract Base Log Model.

.. code-block:: python
    :caption: `models.py`

    from core.models.base import BaseAuditLog

2. Create your new Audit Log  model, inheriting `BaseAuditLog`.
3. Override the `Meta` class `verbose_name` and `verbose_name_plural` with
   a name meaningful to you.

        These names are used in the `Admin panel` amongst other places.

.. caution::

    The new Audit Log must be above your `BaseSoftLogS3Model` or errors can occur.


.. code-block:: python
    :caption: `models.py`

    class MyNewModelAuditLogs(BaseAuditLog):

        class Meta:
            verbose_name = "My New Model Audit Log"
            verbose_name_plural = "My New Model Audit Logs"

|

4. Add the new `BaseSoftLogS3Model` to the Audit Log `log_for_model` field.

.. caution::

    Ensure the ForeignKey to your model is referenced as a string.

    If not unexpected errors will occur.

|

.. code-block:: python
    :caption: `models.py`
    :linenos:
    :emphasize-lines: 1, 7

    class MyNewModelAuditLogs(BaseAuditLog):

        class Meta:
            verbose_name = "My New Model Audit Log"
            verbose_name_plural = "My New Model Audit Logs"

        log_for_model = models.ForeignKey("MyNewModel", on_delete=models.CASCADE)



Add the `_audit_log_model` to your


.. code-block:: python
    :caption: `models.py`
    :linenos:
    :emphasize-lines: 1, 7

    class MyNewModel(BaseSoftLogS3Model):

        class Meta:
            verbose_name = "My New Model"
            verbose_name_plural = "My New Models"

        _audit_log_model = MyNewModelAuditLogs

         # Your custom field names
        field_1 = models.CharField(
                max_length=255,
                blank=False,
                null=False,
            )
        field_2 = models.TextField(
                max_length=1000,
                blank=True,
                null=True,
            )



This completes the setup for your `BaseSoftLogS3Model` to automatically generate
Audit Logs.

|

How it Looks
~~~~~~~~~~~~


Here is how an apps model will look with an audit log.


.. code-block:: python
    :caption: `models.py`

    from core.models.base import (
        BaseSoftLogS3Model,
        BaseAuditLog,
    )

    class MyNewModelAuditLogs(BaseAuditLog):
        """My new audit log docstring"""

        class Meta:
            verbose_name = "My New Model Audit Log"
            verbose_name_plural = "My New Model Audit Logs"


        log_for_model = models.ForeignKey("MyNewModel", on_delete=models.CASCADE)



    class MyNewModel(BaseSoftLogS3Model):
        """My new model docstring"""

        class Meta:
            verbose_name = "My New Model"
            verbose_name_plural = "My New Models"

        _audit_log_model = MyNewModelAuditLogs

         # Your custom field names
        field_1 = models.CharField(
                max_length=255,
                blank=False,
                null=False,
            )
        field_2 = models.TextField(
                max_length=1000,
                blank=True,
                null=True,
            )

|

Views
=====


Your new model has several querysets available and are accessible
when writing views.

For example

.. code-block:: python

    MyNewModel.objects.active()

    MyNewModel.objects.all()

    MyNewModel.objects.archived()

    MyNewModel.objects.deleted()

    MyNewModel.objects.restored()


|

.. rubric:: Further Reading

:ref:`BaseSoftLogS3Model Reference <ref-ABC-base-soft-log-s3>`
