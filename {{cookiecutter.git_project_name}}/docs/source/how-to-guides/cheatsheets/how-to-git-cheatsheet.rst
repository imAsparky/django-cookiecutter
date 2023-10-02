.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-git-cheat-sheet ; Index


.. _how-to-git-cheat-sheet:

===
Git
===

A list of useful commands to help use Git.


Stash
=====


.. _ how-to-git-stash-untracked:

Stash Untracked Files
---------------------

|

To stash your working directory including untracked files and those in the
`.gitignore` use this command.

.. code-block:: bash

    git stash --include-untracked

|

.. _ how-to-git-stash-with-message:

Stash with Message
------------------

|

Stash your working directory with a message for easy indentification when using
`git stash --list`

.. code-block:: bash

    git stash save "Your Stash Message"

|

.. caution::

    `git stash --all` removes all of the files which are `.gitignored`

|

Stash: Search Checkout Copy File
--------------------------------

For a detailed how to see :ref:`How to Stash: Search, Checkout & Copy<how-to-git-search-retrieve-stash>`

|

Staged
======


.. _how-to-git-restore-staged:

Restore Staged Files
--------------------

|

To remove unwanted files that have been added for commit.

.. code-block:: bash

    git restore --staged <filename>

|

.. _how-to-git-reflog-branch:

Reflog Branch
==============

|

Git Reflog lists all commits and past actions.  To reduce the list to just
one branch use the following command.

.. code-block:: bash

    git reflog <branch name>

|


.. _how-to-git-error-gpg-sign-failed:

gpg: signing failed:
====================

|

This error message can be raised when using signed commits.

    gpg: signing failed: Inappropriate ioctl for device


.. code-block:: bash

    export GPG_TTY=$(tty)

|

.. _how-to-git-diff-local-remote:

Diff Local/Remote
=================

|

To see differences between your local branch and your remote-tracking branch.


.. code-block:: bash

    git diff <branch> origin/<branch>

|

.. _how-to-git-pull-remote-file:

Pull Remote File
================

|

Here is how to pull a single file from git remote.

Can also be used to pull a folder by leaving the filename empty.


.. code-block:: bash

    git fetch

.. code-block:: bash

    git checkout origin/<branch-name> -- path/to/file

|

Git Workflow
============

|

Excerpt from `Git Organized: A Better Git Flow` [#]_ that can be adapted to
many situations.

    Imagine this: you’ve been paged to investigate a production incident, and
    after some digging, you identify the commit with the breaking code.
    You decide to revert the change:

    Unfortunately, in doing so, a new bug is introduced! As it turns out, hidden
    in that old “broken” commit was some code that another part of the app depended
    upon, and when you reverted those lines, it left the site once again in a
    broken state. 🙃 Oh dear.

    How can situations like this be avoided? To answer this question, we first
    need to examine how these types of commits come to be.



.. rubric:: Footnotes


.. [#] https://render.com/blog/git-organized-a-better-git-flow
