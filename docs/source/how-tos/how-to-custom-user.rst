.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: cust-user-how-to ; Index

.. _cust-user-how-to:
===========
Custom User
===========

By default, a Custom User employs django-allauth.

The Custom User comes with custom user types.

The CustomUser types have Admin panel filters and are sortable in the
Users view.

All Django Admin security and features remain intact.


Options Before Initial Migration
--------------------------------

CustomUser types can be left as is, or if you wish to change the user types
to meet your needs, change the values in Users/models.py


.. code-block:: python
    :caption: Customise these user types.

    class CustomUser(AbstractUser):

        class CustomUserType(models.TextChoices):
            """Custom user type choices"""

            # Change these to suit your needs before initial migration.
            FREE = "FREE", _("Free")
            LEVEL_1 = "LEVEL 1", _("Level 1")
            LEVEL_2 = "LEVEL 2", _("Level 2")
            STAFF = "STAFF", _("Staff")
            SUPERUSER = "SUPERUSER", _("Superuser")


Accessing Admin Panel
---------------------

Additional security with your Custom User comes by default.

You can only access your new Django project Admin after a successful login.

Placing the Admin panel behind the django-allauth login gives Admin all the
protections of django-allauth.

If this behaviour does not suit your workflow, you can disable this feature by
commenting out the line `admin.site.login`.

.. code-block:: python
    :caption: Users/admin.py

    # Require login before Admin panel is available.  Removes the opportunity for
    # a brute force attack on Admin Login. Provided by django-allauth.
    # https://django-allauth.readthedocs.io/en/latest/advanced.html
    # Comment the following line to disable django-allauth protection
    admin.site.login = login_required(admin.site.login)


Adding a New User
-----------------

When creating a new user with the django-allauth Sign-up form, the Custom User
model is used, and the new user will be required to confirm their email address.

.. note::

    **Adding a new user via the Admin panel**

    After a new user is added with an email address, they will be
    prompted to confirm their email address upon their first sign-in.

    django-allauth provides this functionality.
