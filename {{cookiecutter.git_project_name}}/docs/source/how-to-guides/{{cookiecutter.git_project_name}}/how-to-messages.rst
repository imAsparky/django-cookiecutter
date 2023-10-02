.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-context-processors ; Index


.. _how-to-context-processors:

===============
Django Messages
===============

|

When using django messages, they will be displayed using an alpine element.
They wil work as usual, no special treatment is required.

|

==========================
Django Messages using HTMX
==========================

If you are using HTMX to load in a partial, django messages will not load
because the nav bar is not reloading. Messages can be displayed with HTMX by
using a hx-trigger in the response header.

.. code-block:: python

    def form_valid(self, form):
        self.object = form.save()
        hx_loc = {
            "path": self.request.htmx.current_url_abs_path,
            "target": "#details-container",
        }
        hx_trig = {
            "notify": {
                "type": "info",
                "content": "Account Update Successfully",
            },
            "portUpdate": {},
        }
        return HttpResponse(
            status=204,
            # headers={"HX-Location": json.dumps(hx_loc), "HX-Trigger": "portUpdate"},
            headers={"HX-Location": json.dumps(hx_loc), "HX-Trigger": json.dumps(hx_trig)},
        )

In this instance, there are two hx-triggers being sent back using HTMX. The
relevent code is the "notify" and the dictionary after it. The AlpineJS
messages element is listening out for an event called "notify" where it will
display the contents of the message.
