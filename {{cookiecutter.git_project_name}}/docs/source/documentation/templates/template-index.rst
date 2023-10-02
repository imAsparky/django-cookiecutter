.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: template-index ; Index


.. _template-index:

==============
Index Template
==============

Use the copy button and paste the template into your new index.

|

.. note::

    Change the highlighted line numbers 3, 6 and 8 to suit you use case.

|

.. tip::

    Remove the optional highlighted `toctree` options that aren't required.

    See `Sphinx toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
    for more information about toctree options.

|

.. code-block:: rst
    :caption: **Index Page Template**
    :linenos:
    :emphasize-lines: 2, 5, 7, 14-21

    .. highlight:: rst
    .. index:: template-index ; Index


    .. _template-index:
    ================
    Index Title Here
    ================

    An optional brief description describes the index.


    .. toctree::
       :titlesonly:
       :maxdepth: int
       :hidden:
       :caption:
       :includehidden:
       :reversed:
       :numbered:
       :glob:


.. code-block:: rst
    :caption: **Format to include pages in the TOC**

        to include .rst files in the TOC

        /path-to-first-page
        /path-to-second-page

        to include markdown files in the TOC use the full name with file extension

        /path/to/markdown-file.md
