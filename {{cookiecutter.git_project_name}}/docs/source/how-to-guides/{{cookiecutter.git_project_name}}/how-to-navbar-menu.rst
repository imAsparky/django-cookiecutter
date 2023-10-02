.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-navbar-drop-down ; Index


.. _how-to-navbar-drop-down:

=========================
Navbar: Add Dropdown Menu
=========================

A well organised Navbar menu improves a user’s experience.

Overview
========

As a project grows, adding drop-down menus makes the Navbar HTML code long and
challenging to read.

Add the necessity to ensure correct access to logged-in users; congested
code can make mistakes easier.

Each drop down has been isolated into individual html files to make them more
manageable and easier to maintain.

|

.. _how-to-create-drop-down:

Create Drop-down Menu
=====================

Drop-down menus have individual dedicated HTML files and a standard naming format.

|

.. code-block:: bash

    ./templates/home/navigation/menus/apps.html
    ./templates/home/navigation/menus/notifications.html
    ./templates/home/navigation/menus/user.html

|

In most cases, it would be a simple matter of copying an existing menu item and
it as a template for the new menu item. The templates are well documented, showing
each section of the dropdown, making it easy to know where you are in menu.

Where an icon is needed, SVGs can be found at: HeroIcons_.

.. _HeroIcons: https://heroicons.com/
