.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: security-fail2ban ; Index

.. _how-to-security-fail2ban:

===================
Security - Fail2Ban
===================



What is Fail2Ban
================

extract from Fail2Ban website

Fail2Ban scans log files like /var/log/auth.log and bans IP addresses
conducting too many failed login attempts. It does this by updating system
firewall rules to reject new connections from those IP addresses for a
configurable amount of time. Fail2Ban comes out-of-the-box ready to read many
standard log files, such as those for sshd and Apache, and readily configured
to read any log file of your choosing for any error you wish.

Though Fail2Ban can reduce the rate of incorrect authentication attempts,
it cannot eliminate the risk presented by weak authentication.
Set up services to use only two factor or public/private authentication
mechanisms if you want to really protect services.


Install and Default Configure
-----------------------------

Log into your server.

Update the server and install Fail2Ban.

.. tab:: Ubuntu Server

    .. code-block:: bash

       sudo apt update
       sudo apt upgrade
       sudo apt install fail2ban


    Check fail2ban has installed.

    .. code-block:: bash

        sudo systemctl status fail2ban

    Example output.

    .. code-block:: bash

        ● fail2ban.service - Fail2Ban Service
            Loaded: loaded (/lib/systemd/system/fail2ban.se>
            Active: active (running) since Fri 2021-11-26 0>
            Docs: man:fail2ban(1)
            Process: 636 ExecStartPre=/bin/mkdir -p /run/fai>
          Main PID: 650 (f2b/server)
            Tasks: 5 (limit: 1136)
            Memory: 14.9M
            CGroup: /system.slice/fail2ban.service
                    └─650 /usr/bin/python3 /usr/bin/fail2ba>


    Check what fail2ban is doing for us.

    .. code-block:: bash

        sudo fail2ban-client status


    Example output, showing 1 jail is in use and that is sshd.
    Monitoring sshd is a default setting fail2ban comes with out of the box.

    .. code-block:: bash

        Status
        |- Number of jail:	1
        `- Jail list:	sshd


    Move to the root users fail2ban config folder.

    .. code-block:: bash

        sudo cd etc/fail2ban/
        sudo ls

    Example output

    .. code-block:: bash

        action.d       jail.d
        fail2ban.conf  paths-arch.conf
        fail2ban.d     paths-common.conf
        filter.d       paths-debian.conf
        jail.conf      paths-opensuse.conf


    Copy jail.conf to jail.local. The local folder is the preferred way to
    configure fail2ban. The reason is that jail.conf may be overwriten during
    updates.

    .. code-block:: bash

        sudo cp jail.conf jail.local

    Using your favourite text editor, you can inspect and edit jail.local
    to suit your configuration needs.

    Under the JAILS section, items in [brackets] are options you can enable.
    See `line 291` as an example of an enabled option.
    Everything below the bracketed option is the configuration for that option.
    Line numbers are indicative and may be different in your editor.

     .. code-block:: bash
        :emphasize-lines: 20

            272 # JAILS
            273 #
            274
            275 #
            276 # SSH servers
            277 #
            278
            279 [sshd]
            280
            281 # To use more aggressive sshd modes set filter pa    rameter "mode" in jail.local:
            282 # normal (default), ddos, extra or aggressive (co    mbines all).
            283 # See "tests/files/logs/sshd" or "filter.d/sshd.c    onf" for usage example and details.
            284 #mode   = normal
            285 port    = ssh
            286 logpath = %(sshd_log)s
            287 backend = %(sshd_backend)s
            288
            289
            290 [dropbear]
            291 enabled = true
            292 port     = ssh
            293 logpath  = %(dropbear_log)s
            294 backend  = %(dropbear_backend)s
            295
            296
            297 [selinux-ssh]
            298
            299 port     = ssh
            300 logpath  = %(auditd_log)s
            301
            302`


    Restart fail2ban.

    .. code-block:: bash

        sudo systemctl restart fail2ban


    Check fail2ban status.

    .. code-block:: bash

        sudo fail2ban-client status


    Example output after updating and saving jail.local, notice the new service
    `dropbear`` has been enabled in `Jail list:`.

    .. code-block:: bash

        Status
        |- Number of jail:	2
        `- Jail list:	dropbear, sshd


    Inspect fail2ban log file.

    .. code-block:: bash

        sudo cat /var/log/fail2ban.log


    Example output

    .. code-block:: bash

        --------------------------------------------------
        2021-11-26 06:11:47,432 fail2ban.server         [3089]: INFO    Starting Fail2ban v0.11.1
        2021-11-26 06:11:47,434 fail2ban.observer       [3089]: INFO    Observer start...
        2021-11-26 06:11:47,439 fail2ban.database       [3089]: INFO    Connected to fail2ban persistent database '/var/lib/fail2ban/fail2ban.sqlite3'
        2021-11-26 06:11:47,440 fail2ban.jail

        2021-11-26 05:45:02,953 fail2ban.jail           [2566]: INFO    Jail 'dropbear' uses pyinotify {}
        2021-11-26 05:45:02,957 fail2ban.jail           [2566]: INFO    Initiated 'pyinotify' backend
        2021-11-26 05:45:02,963 fail2ban.filter         [2566]: INFO      maxRetry: 5
        2021-11-26 05:45:02,963 fail2ban.filter         [2566]: INFO      findtime: 600
        2021-11-26 05:45:02,964 fail2ban.actions        [2566]: INFO      banTime: 600
        2021-11-26 05:45:02,964 fail2ban.filter         [2566]: INFO      encoding: UTF-8


    Inspect fail2ban individual jail.

    .. code-block:: bash

        sudo fail2ban-client status sshd

    Example output

    .. code-block:: bash

        Status for the jail: sshd
        |- Filter
        |  |- Currently failed:	1
        |  |- Total failed:	1
        |  `- File list:	/var/log/auth.log
        `- Actions
            |- Currently banned:	0
            |- Total banned:	0
            `- Banned IP list:


Further Reading
---------------

Here is an excellent YouTube tutorial video on the subject.

LearnLinuxTV `Securing your Cloud Server with Fail2Ban`_.




.. _Securing your Cloud Server with Fail2Ban: https://www.youtube.com/watch?v=WMYVqUGMAHM
