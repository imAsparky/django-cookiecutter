.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-git-search-retrieve-stash ; Index


.. _how-to-git-search-retrieve-stash:

==============================
Git Search Retrieve from Stash
==============================

|

Finding and retrieving files from within old stash's can be fiddly. This
short script and useage makes it a breeze.

|

Add Search to Git Config
------------------------

|

Add this script to your local git config file `.git/config`.

.. code-block:: bash

    [alias]
    stashgrep = "!f() { for i in git stash list --format=\"%gd\" ;
    do git stash show -p @" ; done ; }; f"

Credits to `Stackflow Answer 32`_ for the search script.

.. _Stackflow Answer 32: https://stackoverflow.com/questions/42555410/is-it-possible-to-search-through-git-stash-items

|

Search Stash
------------

|

Here are some examples of using the search function from the command line
in the format `git stashgrep <search string>`.

|

.. code-block:: bash

    git stashgrep "filename.py"

    git stashgrep "def some_function()"

|

.. note::

    If spaces exist in the search string, you must use enclosing "".

|

.. _ how-to-git-stash-checkout-file:

Stash: Checkout a Single File
-----------------------------

|

This method will check out the file from the stash into your working branch.
Ensure no uncommitted local changes on the existing file that you do not wish
to lose.

This method will restore the file version when the target stash was performed,
and if there are any differences since the stash, they will be overwritten.

Change the stash number to your target stash.

.. code-block:: bash
    :caption: Checkout stash file.

    git checkout stash@{0} -- <filename>

|

.. _ how-to-git-stash-copy-file:

Stash: Copy File
----------------

|

This non-destructive method will let you recreate the file in the stash into
the working branch under a new filename, removing the risk of overwriting changes.

Change the stash number to your target stash.

|

.. code-block:: bash
    :caption: Copy stashed file to new name.

    git show stash@{0}:stashed_file.rst > copy_of_stashed_file.rst
