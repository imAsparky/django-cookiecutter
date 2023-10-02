.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: template-tutorial ; Index

.. _template-tutorial:

=================
Tutorial Template
=================

Use the copy button and paste the template into your new tutorial.

See the rst code in `Template with Examples`
rendered :ref:`here <rendered-template-tutorial>`.

.. important::

    The highlighted items are the template parts to modify for your use case.

    Examples provided in the `Tutorial body` are for demonstration
    purposes.

    Delete any examples that you wish to.

.. tab:: Template with Examples

    .. code-block:: rst
        :caption: **Highlighted lines require author input.**
        :linenos:
        :emphasize-lines: 3, 6, 8, 13, 37, 43, 44, 47

        .. highlight:: rst
        .. index:: template-tutorial ; Index


        .. _template-tutorial:
        ================
        Name of Tutorial
        ================

        |

        A brief description about the tutorials aims.

        .. admonition:: Example - Using Admonitions

            Use notes to bring something to the user's attention where it improves
            user experience.

            See `Write a tutorial using Diataxis <https://junction-box.readthedocs.io/en/
            latest/Document-Framework/diataxis-tutorials.html>`_
            for assistance on how to write a well-structured tutorial.

        |

        Pre-requisites
        ==============

        Examples of pre-requisites

        `Python 3.6 <https://www.python.org/downloads/>`_ or greater installed on
        your computer.

        :ref:`Create an index page.<template-index>`


        .. _the-name-tutorial:
        Tutorial
        ========



        .. _first-step-title:
        First Step Title
        ----------------

        Select the tab for your preferred Operating System.

        .. admonition:: Example - Using Admonitions

            You can use numbered step headings; however, well-described titles appear
            to flow in the TOC.

            Using Tabs can condense the page and group logical items together,
            for example, different Operating Systems have various commands
            to achieve the same outcome.

            See this example below.

        .. tab:: Linux

            Do some linux command.

        .. tab:: macOS

            Do some macOS command.

        .. tab:: Windows

            Do some Windows command.

        Whats next?
        -----------

        .. hint::

            Here you can guide the user to expand their knowlege with relevant
            information.

            For example:

            See `Diataxis Introduction <https://junction-box.readthedocs.io/en/latest/Document-Framework/diataxis-intro.html>`_
            for more information about writing documentation.

.. tab:: Template Framework Only

    .. code-block:: rst
        :caption: **Highlighted lines require author input.**
        :linenos:
        :emphasize-lines: 3, 6, 8, 13, 22, 28, 29

        .. highlight:: rst
        .. index:: template-tutorial ; Index


        .. _template-tutorial:
        ================
        Name of Tutorial
        ================

        |

        A brief description about the tutorials aims.

        |

        Pre-requisites
        ==============

        |

        .. _the-name-tutorial:
        Tutorial
        ========

        |

        .. _first-step-title:
        First Step Title
        ----------------

        |

        Whats next?
        -----------
