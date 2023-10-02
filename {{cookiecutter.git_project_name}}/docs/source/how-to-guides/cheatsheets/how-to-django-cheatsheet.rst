.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-django-cheat-sheet ; Index


.. _how-to-django-cheat-sheet:

======
Django
======


A list of useful commands to help use Django.


.. _ how-to-django-model-circ-ref:

Model: Circular Reference
=========================

Sometimes when writing models, you may find a situation where you wish to use
a model below the current model or from a different app as a `models.ForeignKey`.

A common use case, but will produce one of several errors due to the referenced
model not being in scope, which is a constraint placed at the SQL level.


.. code-block:: python
    :caption: **Raises Error**
    :linenos:
    :emphasize-lines: 5

    from django.db import models

    class Model1(models.Model):

        model_2 = models.ForeignKey(Model2, on_delete= models.CASCADE)

        field_1 = models.TextField(max_length=255)


    class Model2(models.Model):


        field_1 = models.TextField(max_length=255)

|


Django provides the means to handle this situation, which requires a small
change to referencing the Foreign Key as a string.


This sort of reference, called a lazy relationship, can be helpful when
resolving circular import dependencies between two applications.

Behind the scenes, Django appends “_id” to the field name to create its
database column name.


See `Django Relationship Fields` [#]_ documentation.


.. code-block:: python
    :caption: **Resolves Error**
    :linenos:
    :emphasize-lines: 5

    from django.db import models

    class Model1(models.Model):

        model_2 = models.ForeignKey("Model2", on_delete= models.CASCADE)

        field_1 = models.TextField(max_length=255)


    class Model2(models.Model):


        field_1 = models.TextField(max_length=255)

|

.. _how-to-django-list-model-fields:

Model: List Fields
==================

Get a list of a models fields.


See `Django Model_meta API` [#]_

.. code-block:: python

    from myapp.model import MyModel

    # Get just the model fields

    MyModel._meta.fields

    # or get model fields and relationships.

    MyModel._meta.get_fields()


    # or Returns the field instance given a name of a field.

    MyModel._meta.get_fields("username")



    # A non existent field
    >>>MyModel._meta.get_field('does_not_exist')
    Traceback (most recent call last):
        ...
    FieldDoesNotExist: MyModel has no field named 'does_not_exist'

|

.. _how-to-django-migrations-sync:

Migration: Syncronising
=======================

Synchronising migrations between development and production servers can become
challenging after running many migrations locally.

A simple means to keep migrations synchronised for existing apps is to follow
these steps before pushing to git:

#. Change directory to the app root folder.
#. Delete the app's local migrations folder.
#. Pull (checkout) the main branch migrations folder. See bash code below.
#. `./manage.py makemigrations`
#. Include the migrations in your git commit and push.

.. code-block:: bash

    git checkout origin/main app_name/migrations



|

.. rubric:: Footnote

.. [#] https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
.. [#] https://docs.djangoproject.com/en/4.0/ref/models/meta/
