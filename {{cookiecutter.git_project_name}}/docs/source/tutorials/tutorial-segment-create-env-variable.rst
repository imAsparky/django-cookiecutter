.. _create-env-var-segment:

Create Django Secret Environment Variable
-----------------------------------------

In settings.py,  the Django secret key configuration is in an environment
variable.  See below.


.. code-block:: python

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ("DJANGO_SECRET_KEY")


Create a Django Secret key.

.. code-block::

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

You will see an output similat to this.

.. code-block::

    w#5cb$au3$t+hyj(f7ejgrk7$xet7_q@8m)5qd*c_*)nl1shwr

.. danger::

  DO NOT USE THE `NO LONGER` SECRET KEY GENERATED HERE.


Copy and add the secret key to an environment variable.


.. tab:: Linux

    .. code-block:: bash
        :caption: **bash/zsh**

        export DJANGO_SECRET_KEY='w=#5cb$au3$t+hyj(f7ejgrk7$xet7_q@8m)5qd*c_*)nl1shwr'

    .. code-block:: bash
        :caption: **bash/zsh**

        printenv DJANGO_SECRET_KEY  # To check it worked

    .. code-block:: bash
        :caption: **bash/zsh**

        w#5cb$au3$t+hyj(f7ejgrk7$xet7_q@8m)5qd*c_*)nl1shwr


.. tab:: macOS


    .. code-block:: bash
        :caption: **bash/zsh**

        export DJANGO_SECRET_KEY='w=#5cb$au3$t+hyj(f7ejgrk7$xet7_q@8m)5qd*c_*)nl1shwr'

    .. code-block:: bash
        :caption: **bash/zsh**

        printenv DJANGO_SECRET_KEY  # To check it worked

    .. code-block:: bash
        :caption: **bash/zsh**

        w#5cb$au3$t+hyj(f7ejgrk7$xet7_q@8m)5qd*c_*)nl1shwr

.. tab:: Windows

    #. Right-click the Computer icon and choose Properties, or in
       Windows Control Panel, choose System.

    #. Choose Advanced system settings.

    .. image:: ../_static/tutorials/segment-create-env-variable/windows-system-properties.png
       :alt: Windows System Properties


    #. On the Advanced tab, click Environment Variables.

    .. image:: ../_static/tutorials/segment-create-env-variable/windows-environ-variables.png
       :alt: Windows Environment Variables


    #. Click New to create a new environment variable.
    #. After creating or modifying the environment variable, click Apply
       and then OK to have the change take effect.


    .. note::

        The graphical user interface for creating environment variables may
        vary slightly, depending on your version of Windows.
