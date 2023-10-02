.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-template-pop-up-modal ; Index


.. _how-to-template-pop-up-modal:

======================
Template: Pop Up Modal
======================

Overview
========

While using HTMX, it is possible to have a lot of partial HTML files for swapping
in and out different elements. A lot of this HTML will be duplicated in each
partial. Additionally, where a user input is required and then default flow
of the app is to return to the original page, it is a smoother experience to not
get navigated away from that page.

Using a pop up modal solves both of these issues. However this does require a
slightly different flow of code in the views.py file. This How To will consider
the example of the user profile settings form.

|

Standard HTMX Flow
==================

The standard flow of using HTMX would be to have a full page template as well as
a partial file that would only contain the HTML to be swapped into the DOM on a
HTMX request. When the request to the server is a standard GET, the full template
is loaded, if the server recieves a HTMX request then the partial will be returned
and HTMX will swap the approriate area of the DOM with the new HTML.

The code block below would be all that is required for a standard HTMX user
settings page to be loaded to the user.

|

.. code-block:: python
    :caption: users/views.py
    :linenos:

    from django.contrib.auth.mixins import LoginRequiredMixin
    from core.views.generic.edit import HtmxUpdateView

    from .forms import CustomUserChangeForm
    from .models import CustomUser

    class CustomUserSettings(LoginRequiredMixin, HtmxUpdateView):
        model = CustomUser
        htmx_template_name = "users/partials/user_settings.html"
        template_name = "home/user_settings.html"
        success_url = reverse_lazy("home:landing")
        form_class = CustomUserChangeForm

|

Using the Pop Up Modal
======================

Loading the new HTML into the pop up modal is the same as using HTMX as normal.
On the button that will send the request, the target should be #dialog. See the
user menu code snippet below.

In the HTML that is sent to be displayed in the modal, there is no need to provide
any wrapper divs. See the user settings form code snippet below. Any button that
will submit the data to the server will need to use HTMX. Where a button will be
used to cancel the form, no input is needed from the server. Just add the @click
AlpineJS as seen in the user settings form.

Here is where the standard HTMX flow deviates.

When the form is submitted, we don't want to send back a response that is going
result in a redirect. Additionally, HTMX will only make changes to the DOM on a
200 response from the server. We can leverage this to control how the user page
is updated on a successful submit. In the view code below you can see that on a
successful form save, a 204 response is returned. In addition, an optional
HX-Header is returned.

The 204 response will trigger the modal to close and any optional HX-Headers
will be executed by HTMX. See `HTMX Response Headers`_ for all of the available
options.

.. note:: For the escape key to close the modal, focus needs to be on something
    in the modal. For this reason, something that is displayed on the modal will
    need to have the autofocus attribute.

.. _HTMX Response Headers: https://htmx.org/reference/#response_headers

|

.. code-block:: python
    :caption: users/views.py
    :linenos:

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

.. code-block:: html+django
    :caption: templates/home/navigation/menus/user.html
    :linenos:
    :emphasize-lines: 3, 4

    {% raw %}
    <!-- User profile -->
    <a hx-get="{% url 'users:settings' user.id %}"
    hx-target="#dialog"
    hx-push-url="false"
    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
    role="menuitem"
    tabindex="-1"
    id="user-menu-item-0">{% trans "Your Profile" %}</a>
    {% endraw %}

|

.. code-block:: html+django
    :caption: templates/users/forms/user_settings.html
    :linenos:
    :emphasize-lines: 9, 10

    {% raw %}
    <form method='POST' action="{{ request.path }}">
        {% csrf_token %}
        {{form.as_p}}
        <div class="flex">
            <p class="pt-4">Passsword: </p>
            <a href="{% url 'account_reset_password' %}" type="button" class="p-2 mt-2 ml-1 border border-black rounded-2xl bg-slate-300 hover:bg-slate-100 w-80">Change</a>
        </div>
        <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
            <button type="button" hx-post="{% url 'users:settings' user.id %}" class="inline-flex justify-center w-full px-4 py-2 text-base font-medium text-white bg-indigo-600 border border-transparent rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm">Submit</button>
            <button type="button" @click="$store.displayModal.hideModal()" class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm">Cancel</button>
        </div>
    </form>
    {% endraw %}

|

What Is Happening In Browser
============================

Lets first look at base.html to understand how this is working in the browser.

There is a small amount of JS required to get this to work, a combination of
AlpineJS and HTMX. When the page first fully loads, an AlpineJS variable is
initialised called displayModal.on and two functions provided to modify that
variable. When showModal is called, displayModal.on is set to true. When hideModal
is called, displayModal.on is set to false and the HTML that was dispalyed in
modal is cleared. This clearing of the HTML will prevent a potential flash of old code
showing before the new HTML is swapped in. This is all that is needed to show
and hide the modal.

In order for HTMX to be able to show and hide the modal, HTMX and AlpineJS need
to be wired together. By using event listeners from HTMX, we can call showModal
and hideModal as required. For example, on the event htmx:afterswap, if the
target is #dialog, then run showModal. Additionally, on the event htmx:beforeSwap
if the target is #dialog and the response is not 200, then run hideModal.

|

.. code-block:: html
    :caption: templates/base.html
    :linenos:

    {% raw %}
    <!-- This script creates the variable for showing and hiding the dialog box -->
    <script>
      htmx.on("htmx:afterSwap", (e) => {
        // Response targeting #dialog => show the modal
        if (e.detail.target.id == "dialog") {
          Alpine.store('displayModal').showModal();
        }
      }),
      htmx.on("htmx:afterOnLoad", (e) =>{
        if(e.detail.target.id == "dialog" && !e.detail.xhr.response){
          Alpine.store('displayModal').hideModal();
        }
      })
      htmx.on("htmx:afterOnLoad", (e) =>{
        if(!e.detail.xhr.response){
          Alpine.store('displayModal').hideModal();
        }
      })
    </script>

    <!-- This script adds HTMX event listeners to show/hide the dialog box -->
    <script>
      document.body.addEventListener('htmx:afterSwap', function(e) {
        if (e.detail.target.id === "dialog"){
            Alpine.store('displayModal').showModal();
        }
      }),
      document.body.addEventListener('htmx:beforeSwap', function(e) {
        if (e.detail.target.id === "dialog" && !e.detail.xhr.response){
            Alpine.store('displayModal').hideModal();
        }
      }),
      document.body.addEventListener('htmx:beforeSwap', function(e) {
        if (!e.detail.xhr.response){
            Alpine.store('displayModal').hideModal();
        }
      })
    </script>

    {% endraw %}

|

Now lets look at the AlpineJS elements in the modal itself. When the variable
displayModal.on is set to true, the modal will be displayed by x-show. That is
all there is to model itself.

|

.. code-block:: html
    :caption: templates/home/partials/modal.html
    :linenos:

    {% raw %}
    <div x-data @keyup.escape="$store.displayModal.hideModal()">
        <div x-show="$store.displayModal.on" x-transition class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
            <div class="fixed inset-0 transition-opacity bg-gray-500 bg-opacity-75"></div>
            <div class="fixed inset-0 z-10 overflow-y-auto">
            <div class="flex items-end justify-center min-h-full p-4 text-center sm:items-center sm:p-0">
                <div class="relative px-4 pt-5 pb-4 overflow-hidden text-left transition-all transform bg-white rounded-lg shadow-xl sm:my-8 sm:max-w-lg sm:w-full sm:p-6">
                <div id="dialog" x-transition>
                    <!-- Inject HTML here -->
                </div>
                </div>
            </div>
            </div>
        </div>
    </div>
  {% endraw %}


Using the modal with forms
==========================

When using a form in the modal, there could be feedback when the form is not
valid. In this case, we only want the modal to close when the form is valid.
To achieve this, the button used to submit the form should set
hx-target:"#dialog". See the code block below as an example form.

In the case of a valid form, a non-200 response is sent from the view, which
will close the modal. In the event of an invalid form, the server sends a html
response which will be displayed in the modal.

|

.. code-block:: html+django
    :caption: templates/organisation/portfolio/forex/partials/forex_account_create_view.html
    :linenos:

    {% raw %}
    <span class="flex justify-center pb-2">
        <strong class="font-bold">Forex Account Create View</strong>
    </span>

    <form method='POST' action="{{ request.path }}">
        {% csrf_token %}

        {% include 'home/partials/form_layout.html' %}

        <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
            <button type="button" hx-post={% url 'forex:account_create' portfolio %} hx-target="#dialog" hx-vals="js:{org_select: document.getElementById('org-select').value}" class="inline-flex justify-center w-full px-4 py-2 text-base font-medium text-white bg-indigo-600 border border-transparent rounded-md shadow-sm dark:bg-gray-500 dark:hover:bg-gray-400 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm">Submit</button>
            <button type="button" @click="$store.displayModal.hideModal()" class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm dark:bg-gray-100 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm">Cancel</button>
        </div>
    </form>
    {% endraw %}
