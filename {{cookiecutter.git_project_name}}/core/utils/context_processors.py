"""Django context processors."""

import environ
{% if cookiecutter.allow_new_user_signup != "n" %}
from constance import config
{% endif %}
from django.conf import settings

from users.models import CustomUser

env = environ.FileAwareEnv()


def export_vars(request) -> dict:
    """Export environment variables to Django templates.

    https://stackoverflow.com/questions/43207563/how-can-i-access-environment-variables-directly-in-a-django-template/43211490#43211490?newreg=9f02cb1a210c4f618f41fb1759bd9fb3

    Useage
    ------

    An example of how to access the environment variable in the template using
    just the data dict key to pass the CSS file location to the template.

    {% raw %}
    <link rel="stylesheet" href="{{ CSS }}">
    {% endraw %}

    """

    data: dict = {}

    data["PROJECT_NAME"] = "{{ cookiecutter.project_name }}"

    {% if cookiecutter.dynamically_set_css_in_templates != "n" %}
    if settings.SETTINGS_MODULE == "config.settings.production":
        data["CSS"] = env("PROD_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css")
        data["TAILWIND_CSS_DEV"] = env("PROD_TAILWIND_CSS_DEV", default=False)

    elif settings.SETTINGS_MODULE == "config.settings.staging":
        data["CSS"] = env(
            "STAGING_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css"
        )
        data["TAILWIND_CSS_DEV"] = env("STAGING_TAILWIND_CSS_DEV", default=False)

    else:
        data["CSS"] = env(
            "LOCAL_DJANGO_TEMPLATES_CSS", default="/static/css/styles.css"
        )
        data["TAILWIND_CSS_DEV"] = env("LOCAL_TAILWIND_CSS_DEV", default=True)
    {% endif %}

    {% if cookiecutter.show_env_in_templates != "n" %}
    # Passes environment and debug status to be displayed on webpage.
    match settings.SETTINGS_MODULE:
        case "config.settings.local":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "LOCAL: Debug True"

            else:
                data["ENVIRONMENT"] = "LOCAL: Debug False"

        case "config.settings.production":
            data["ENVIRONMENT"] = "PRODUCTION"

        case "config.settings.staging":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "STAGING: Debug True"
            else:
                data["ENVIRONMENT"] = "STAGING: Debug False"

        case "config.settings.test":
            if settings.DEBUG:
                data["ENVIRONMENT"] = "TESTING: Debug True"
            else:
                data["ENVIRONMENT"] = "TESTING: Debug False"

        case _:
            environ = settings.SETTINGS_MODULE.rsplit(".", 1)[-1].upper()

            if settings.DEBUG:
                data["ENVIRONMENT"] = f"{environ}: Debug True"
            else:
                data["ENVIRONMENT"] = f"{environ}: Debug False"
    {% endif %}
    {% if cookiecutter.allow_new_user_signup != "n" %}
    data["ALLOW_NEW_USER_SIGNUP"] = config.ALLOW_NEW_USER_SIGNUP
    {% endif %}


    return data
