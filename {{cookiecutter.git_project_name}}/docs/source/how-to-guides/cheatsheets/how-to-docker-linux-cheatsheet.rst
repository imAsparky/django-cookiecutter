.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-cli-cheat ; Index

.. _how-to-cli-cheat:

=====================
Linux CLI Cheat Sheet
=====================

.. _how-to-cli-cheat-docker:

Docker
======

A selection of useful Docker CLI commands, with copy button convenience.


Show me
-------

.. tab:: Containers

    .. code-block:: bash
        :caption: List all containers.

        docker containers

.. tab:: Images

    .. code-block:: bash
        :caption: List all images.

        docker image ls

.. tab:: Networks

    .. code-block:: bash
        :caption: List all networks.

        docker network ls

.. tab:: Volumes

    .. code-block:: bash
        :caption: List all volumes.

        docker volume ls

.. tab:: System

    .. code-block:: bash
        :caption: List all running containers.

        docker ps

Stop
----

.. code-block:: bash
    :caption: Stop one running container.

    docker stop <container-id>


.. code-block:: bash
    :caption: Stop all running containers.

    docker stop $(docker ps -a -q)

Prune / Delete
--------------

Docker takes a conservative approach to remove unused objects.  Items such as
images, containers, volumes, and networks are generally not removed unless you
explicitly ask Docker to do so. The result is Docker uses extra disk space.

To solve this problem, Docker provides a prune command for each type of object.
Docker also provides `docker system prune` [#]_ to clean up multiple types
of objects at once.

See a selection of the most commonly used Docker commands for the development
of the django-cookiecutter project below.

|

.. tab:: Containers

    .. code-block:: bash
        :caption: WARNING! This will remove all stopped containers.

        docker container prune

.. tab:: Images

    .. code-block:: bash
        :caption:  WARNING! This will remove all dangling images.

        docker image prune

    .. code-block:: bash
        :caption:  WARNING! This will remove all images without at least one container associated to them.

        docker image prune -a

.. tab:: Networks

    .. code-block:: bash
        :caption: WARNING! This will remove all networks not used by at least one container.

        docker network prune


.. tab:: Volumes

    .. code-block:: bash
        :caption: WARNING! This will remove all volumes not used by at least one container.

        docker volume prune

.. tab:: System

    .. admonition:: One command to rule them all...

        Suppose you want to do a major cleanup with one command.

        Ensure nothing happens to your production stack;
        **make sure your production stacks are running.**

    .. warning::

        WARNING! This will remove:

        - all stopped containers.

        - all networks not used by at least one container.

        - all dangling images.

        - all dangling build cache.


    .. code-block:: bash

        docker system prune

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _how-to-cli-cheat-linux-win:

Linux-macOS-Windows
===================

A selection of useful CLI commands, with copy button convenience.

.. _how-to-cli-cheat-check-ports:

Check Ports
-----------

.. tab:: Linux

    Useage options: `LISTEN`, `ESTABLISHED` and `CLOSED`.

    .. code-block:: bash

        sudo lsof -i -P -n | grep LISTEN

    .. code-block:: bash

        sudo lsof -i:22 ## see a specific port such as 22 ##

    .. code-block:: bash

        sudo nmap -sTU -O IP-address-Here

    .. code-block:: bash

        sudo ss -tulpn | grep LISTEN

    .. hint::

        **ss** command options.

        `-t` : Show only TCP sockets on Linux.

        `-u` : Display only UDP sockets on Linux.

        `-l` : Show listening sockets. For example, TCP port 22 is opened by SSHD server.

        `-p` : List process name that opened sockets.

        `-n` : Don’t resolve service names i.e. don’t use DNS.

.. tab:: macOS

      Useage options: `LISTEN`, `ESTABLISHED` and `CLOSED`.

    .. code-block:: bash

       sudo lsof -i -P -n | grep LISTEN

    .. code-block:: bash

        netstat -a -n | grep 'LISTEN '

    .. hint::

        command options.

        `-i` : for IPv4 and IPv6 protocols.

        `-p` : Display raw port number, not resolved names like `ftp`, `http`.

        `-P` : Omit the port names.

        `-n` : Don’t resolve service names i.e. don’t use DNS.

        `-a` : [Netstat] Show all sockets.

        `-n` : [Netstat] Don’t resolve service names i.e. don’t use DNS.

.. tab:: Windows

    .. code-block:: powershell

        netstat -bano | more

    .. code-block:: powershell

        netstat -bano | grep LISTENING

    .. code-block:: powershell

        netstat -bano | findstr /R /C:"[LISTEING]"


.. _how-to-cli-cheat-django-secret-key:

Django Secret Key
-----------------

To generate a Django secret key, in your favourite CLI paste the code below
and hit enter.

.. code-block:: bash

   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


Copy the key generated and exit the python shell.

.. caution::

    If you are storing your secret key in an environment variable.

    In linux style OS the secret key must be enclosed in " ".

    If not an error may be raised and the key may not save.

    .. code-block:: bash

        export SECRET_KEY="YOUR_SECRET_KEY"

See :ref:`here<create-env-var-segment>` for a tutorial about creating
environment variables.

.. rubric:: Footnotes

.. [#] https://docs.docker.com/config/pruning/
