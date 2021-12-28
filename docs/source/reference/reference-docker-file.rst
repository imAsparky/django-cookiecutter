.. highlight:: rst
.. index:: docker-file ; Index

.. _docker-file:
==========
Dockerfile
==========

If a `deploy_with_docker` option is selected when creating your
django-cookiecutter, your new Django Cookiecutter Project includes a
Dockerfile to build a docker image.

The Docker file is modified from the original adaption
`Here's a Production-Ready Dockerfile for Your Python/Django App` [#]_.

See a list of further reading in the FOOTNOTES.

Structure
=========

The Dockerfile is composed of two main areas to reduce the size of the final
production image.

A compile image.

.. code-block:: docker

    FROM python:3.9-slim-bullseye AS compile-image

A production image.

Once the compile-image has completed its build, the production-image copies
only what is required to run a production image.

.. code-block:: docker

    FROM python:3.9-slim-bullseye AS production-image


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Environment Variables
=====================

PYTHONDONTWRITEBYTECODE
-----------------------

The Python interpreter,  by default,  writes bytecode (.pyc) files to disk when
executing code.

The (.pyc) files should not be checked into source control.

Setting `PYTHONDONTWRITEBYTECODE to 1` ensures Python will no longer write
bytecode files (.pyc) to disk. Reducing the size of your Docker image.

PYTHONUNBUFFERED
----------------

Setting `PYTHONUNBUFFERED to 1` ensures the Python output is sent straight to
the terminal, allowing you to see the output of your Django logs in real-time.

Also, if the python application crashes, this ensures no partial output is held
in a buffer and never sent to the terminal.

.. code-block:: docker

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1


uWSGI
-----

`WSGI` [#]_ (pronounced wiz-gee) stands for `Web Server Gateway Interface`,
and it's a specification for the software interface between a web server
and a Python application.

`uWSGI` [#]_ is a popular web server that implements the WSGI standard.

`uwsgi` [#]_ is a binary protocol used by `uWSGI` and mainly works on TCP.

The following ENV_VARS are for configuring the `uWSGI` server.  These shouldn't
need changing; however, if you wish to further customise your Django
application, you can read about uWSGI options [#]_ or uWSGI HTTP [#]_.

.. code-block:: docker

    # Location of your django project wsg.py file.
    ENV UWSGI_WSGI_FILE=django_project/wsgi.py

    ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1
    ENV UWSGI_WORKERS=2 UWSGI_THREADS=4
    ENV UWSGI_STATIC_MAP="/static/=/code/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

`The Art of Graceful Reloading` [#]_ provides information about reloading your
Django application.   See `Dealing with ultra-lazy apps (like Django)` in that
article for more details if you are experiencing slow application reloads.


If your django project needs nginx as well for heavy loads
see this tutorial `Setting up Django and your web
server with uWSGI and nginx` [#]_.

`nginx` [#]_ (pronounced engine-x) is a free, open-source, high-performance HTTP
server, reverse proxy and IMAP/POP3 proxy server.


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Run Commands
============

User
----

By default, Docker containers run as the root user. Running a Docker container
as `root` is insecure in production and increases the ability for a
`Docker escalation attack` [#]_.

Setting an `APP_User` reduces the ability for bad actors to do damage, and
setting `WORKDIR` to `APP_USER` reduces file access permission problems.

.. code-block:: docker

    ARG APP_USER=django
    RUN groupadd -r ${APP_USER} \
                 && useradd -m --no-log-init -r -g ${APP_USER} ${APP_USER}

    WORKDIR /home/${APP_USER}


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

|


.. rubric:: Footnotes

.. [#] https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
.. [#] https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/index.html
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/Options.html
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/HTTP.html
.. [#] https://uwsgi-docs.readthedocs.io/en/latest/articles/TheArtOfGracefulReloading.html#dealing-with-ultra-lazy-apps-like-django
.. [#] http://nginx.org/
.. [#] https://pythonspeed.com/articles/root-capabilities-docker-security/
