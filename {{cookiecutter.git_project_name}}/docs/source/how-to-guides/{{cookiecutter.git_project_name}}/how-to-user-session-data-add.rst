.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-user-session-data-add ; Index


.. _how-to-user-session-data-add:

============================
User: Adding to Session Data
============================

Overview
========

Where there are global user settings that will need to be access throughout the
app, the user session could be the best place to store that information. This
`how-to-guide` will look at two different situations, where the user changes settings and
the session data needs to be updated and when the user logs in, adding the data
to the user session. Both examples will look at the user timezone settings, see
the code below.

|

User Updates Their Settings
===========================

When the user changes their settings in a form, updating the user session is as
simple as updating the session data in the request. See line 26.

|

For a good tutorial on using session data see this MDNWebDocs_.

.. _MDNWebDocs: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions

|
|

User Logs In
============

When the user logs in Django does not know what data needs to be loaded into
the session. Django-AllAuth uses signals that can be used to trigger adding the
data in. In this case, the user_logged_in signal passes the request and the
user, so it is just a case of mapping the user data to the session. See line 33.

|

To see all the Django-AllAuth signals that can be used, see Signals_.

.. _Signals: https://django-allauth.readthedocs.io/en/latest/signals.html

|
|

.. code-block:: python
    :caption: users/views.py
    :linenos:
    :emphasize-lines: 26, 31-33


    from allauth.account.signals import user_logged_in
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.dispatch import receiver
    from django.http import HttpResponse
    from django.urls import reverse_lazy

    from core.views.generic.edit import HtmxUpdateView

    from .forms import CustomUserChangeForm
    from .models import CustomUser

    # Create your views here.


    class CustomUserSettings(LoginRequiredMixin, HtmxUpdateView):
        model = CustomUser
        htmx_template_name = "users/forms/user_settings.html"
        template_name = "home/landing.html"
        success_url = reverse_lazy("home:landing")
        form_class = CustomUserChangeForm

        # Where the form is valid, save it and update the session timezone.
        # This will also tell HTMX to refresh the page to load the new timezone
        # into the user session which will update any times on the page.
        def form_valid(self, form):
            self.request.session["timezone"] = form.instance.timezone
            self.object = form.save()
            return HttpResponse(status=204, headers={"HX-Refresh": "true"})

        # When the user logs in, add the timezone to the user session
        @receiver(user_logged_in)
        def logged_in(request, user, **kwargs):
            request.session["timezone"] = user.timezone

|
