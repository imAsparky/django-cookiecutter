"""django-cookiecutter pre package generation jobs."""

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

# languages = "{{ cookiecutter.languages }}".replace(' ', '').split(',')
# for language in languages:
#     assert len(language) == 2 and
# language.lower() == language, "A language code shall contain two lowercase\
#  letters, '" + language + "' doesn't."
# if "{{ cookiecutter.use_i18n }}" == 'y':
#     assert len(languages) > 1, "'use_i18n' contains less than two languages."
# else:
#     assert len(languages) == 1, "If 'use_i18n' is unset, only one language\
#  shall be specified in 'languages'."
