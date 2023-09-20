.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-test-env-settings ; Index

.. _test-env-settings:

=========================
Test Environment Settings
=========================


.. _test-env-settings_override:

Override Settings
=================

|

Override Django settings easily in `tests/conftest.py`.

Add your setting to `TEST_SETTINGS`.

This settings snippet is from Speed Up Your Django Tests by Adam Chainz.
The book is very well written and is a wealth of knowledge.
You can purchase `Speed Up Your Django Tests` from `here`_.

.. _here: https://adamchainz.gumroad.com/l/suydt


.. code-block:: python
    :linenos:
    :caption: tests/conftest.py

    from django.test.utils import override_settings

    @pytest.fixture(scope="session", autouse=True)
    def test_settings():
    """Provide settings override for tests"""
    with override_settings(**TEST_SETTINGS):
        yield


    TEST_SETTINGS = {
        "PAGINATION_COUNT": 10,

    }

|

.. _test-env-settings_databases:

Databases
=========

By default, SQLite is used in the test environment to make it easier for

#. Quick local development without the need to set up Postgress and
#. New Django users.


Using PostgreSQL
----------------

By default PostgreSQL is our preferred option for Production.

If you wish to test using the same environment configuration as production,
you can make changes to /.env/.testing.

#. Change line 7 to `other`.
#. Add your PostgresSQL connection string to line 8, or
#. Create an environment variable DB_URL with your connection string,
   See :ref:`here<create-env-var-segment>` for a tutorial about creating
   environment variables.

.. code-block:: python
    :emphasize-lines: 7, 8
    :caption: /.env/.testing
    :linenos:

    # Testing Environment ENV Keys

    # Testing Environment Django
    TESTING_ALLOWED_HOSTS=*
    # Testing database options: sqlite3, other.
    # If using other, a TESTING_DATABASE_URL connection string must be supplied.
    TESTING_DJANGO_DATABASE=sqlite3
    TESTING_DATABASE_URL=""
    TESTING_DJANGO_DEBUG=False
    TESTING_DJANGO_INTERNAL_IPS=[]
    TESTING_DJANGO_LOG_FILE='logging/rotating_testing.log'
    TESTING_DJANGO_LOGGING_LEVEL='DEBUG'
    TESTING_DJANGO_LOGGING_MAIL_ADMINS='ERROR'

.. warning::

    DB_URL can conflict with your production DB if your testing machine
    and production machine are the same.


Other Databases
---------------

In addition to making the changes in the `Using PostgreSQL` section above the
following changes need to be made.

Three dependency files need to be updated.

#. /config/requirements/test.txt
#. /config/requirements/staging.txt
#. /config/requirements/production.txt

With these changes.

#. Line 3 and line 4 must be commented out or deleted.
#. Add your preferred database's dependencies in these files.


.. code-block:: python
    :emphasize-lines: 3-4
    :caption: Depencies to remove.
    :linenos:

    coverage==6.2
    dj-inmemorystorage==2.1.0
    psycopg2==2.9.3 # This version should be used in production
    # psycopg2-binary  # This version is ok for Development and Testing
    pytest==6.2.5
    pytest-django==4.5.2
    pytest-reverse==1.3.0
    pytest-xdist==2.5.0
    tblib==1.7.0
    tox==3.24.5


Follow any other instructions from your DB vendor for integration with Django.
