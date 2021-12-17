.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-cli-cheat ; Index

.. _how-to-cli-cheat:
===============
CLI Cheat Sheet
===============

.. _how-to-cli-cheat-docker:
Docker
======

A selection of useful Docker CLI commands, with copy button convenience.


Show me
-------

.. tab:: Containers

    .. code-block:: bash
        :caption: List all containers.

        docker container ls

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

Start
-----

.. code-block:: bash
    :caption: Start one docker image in detached mode.

    docker run -d <container-id>


.. code-block:: bash
    :caption: Start several containers with docker compose.

    docker-compose -c <docker-compose filename>

.. code-block:: bash
    :caption: Start a docker swarm.

    docker stack deploy -c  <docker-compose filename> <stack name>

Stop
----

.. code-block:: bash
    :caption: Stop one running container.

    docker stop <container-id>


.. code-block:: bash
    :caption: Stop all running containers.

    docker stop $(docker ps -a -q)


.. code-block:: bash
    :caption: Stop a docker swarm.

    docker stack rm <stack name>

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

    .. code-block:: cmd

        netstat -bano | more

    .. code-block:: cmd

        netstat -bano | grep LISTENING

    .. code-block:: cmd

        netstat -bano | findstr /R /C:"[LISTEING]"

.. _how-to-cli-cheat-gen-rand-passwd:
Random Password
---------------

Generating a random password, you  can modify the password length or use the
generated password's first `n` characters if you don't want such a long
password. Using a password manager saves you from having to memorise them.

Password lengths demonstrated are 32 characters long.

.. tab:: Linux

    .. code-block:: bash

        date +%s | sha256sum | base64 | head -c 32 ; echo

    .. code-block:: bash

        < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;

    .. code-block:: bash

        # If openssl rand function is installed on your system.
        openssl rand -base64 32


.. _how-to-cli-cheat-ENV-vars:
Environment Variables
---------------------

.. TODO:: Add the environment variable tutorial link here.

.. tab:: Linux

    .. tab:: Persisting Environment Variables

        As <root> create /etc/profile.d/<new-env-file>.sh

        This file is for system-wide environment variable settings. It is not a
        script file but instead consists of assignment expressions, one per line.

        Files with the .sh extension in the /etc/profile.d directory gets executed
        with a new bash login shell. E.G. when logging in from the console or over
        ssh, and by the DisplayManager when the desktop session loads.

        .. code-block:: bash
            :caption: Open the file with an editor as <root>.

            vi /etc/profile.d/<new-env-file>.sh

        .. code-block:: vim
            :caption: Add the environment variables.

            export DJANGO_SECRET_KEY=your-secret-django-key
            export POSTGRES_USER=your-postgress-user

    .. tab:: Deleting Environment Variables

        .. code-block:: bash
            :caption: Use unset

            unset DJANGO_SECRET_KEY
            unset POSTGRES_USER


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

    See :ref:`Environment Variables<how-to-cli-cheat-ENV-vars>`
    for more information.

    .. code-block:: bash

        export SECRET_KEY="YOUR_SECRET_KEY"

See :ref:`here<create-env-var-segment>` for a tutorial about creating
environment variables.


.. rubric:: Footnotes

.. [#] https://docs.docker.com/config/pruning/
