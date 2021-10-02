"""
django-cookiecutter pre package generation jobs.

.. todo::

    Replace the LANGUAGES check in pre-gen.py

    Check against available translations
    https://github.com/django/django/blob/main/django/conf/global_settings.py


"""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(
        f"ERROR: The project slug {MODULE_NAME} is not a valid Python module\
            name.  Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)


LANGUAGES = "{{ cookiecutter.LANGUAGES }}".replace(" ", "").split(",")
for language in LANGUAGES:
    assert len(language) == 2 and language.lower() == language, (  # nosec
        "A language code shall contain two lowercase letters, '"
        + language
        + "' doesn't."
    )

# fmt: off
if "{{ cookiecutter.USE_I18N }}" == "y":
    assert (   # nosec
        len(LANGUAGES) > 0
    ), "'USE_I18N' True with empty LANGUAGES list."
else:
    assert (  # nosec
        len(LANGUAGES) == 1
    ), "'USE_I18N' False with entries in LANGUAGES list."
# fmt: on
