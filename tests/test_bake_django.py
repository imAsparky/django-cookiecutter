"""django-cookiecutter test suite."""

import datetime
import os


def test_django_bakes_ok_with_defaults(cookies):
    """Test cookiecutter created the Django project ok."""
    default_django = cookies.bake()

    assert default_django.project_path.is_dir()
    assert default_django.exit_code == 0
    assert default_django.exception == None
    assert default_django.project_path.name == "django-boilerplate"


def test_baked_django_asgi_file(cookies):
    """Test Django asgy.py file has been generated correctly."""
    default_django = cookies.bake()

    asgi_path = default_django.project_path / "django_boilerplate/asgi.py"
    asgi_file = asgi_path.read_text().splitlines()

    assert '"""ASGI config for django-boilerplate project.' in asgi_file
    assert '    "DJANGO_SETTINGS_MODULE", "django_boilerplate.settings"' in asgi_file


def test_baked_django_with_commit_message_file(cookies):
    """Test Django Conventional commit message template has been generated correctly."""
    default_django = cookies.bake()

    assert ".git-commit-template.txt" in os.listdir(
        (default_django.project_path / ".github")
    )


def test_baked_django_without_commit_message_file(cookies):
    """Test Django Conventional commit message template has not been generated."""
    non_default_django = cookies.bake(
        extra_context={
            "create_conventional_commits_edit_message": "n",
        }
    )

    assert ".git-commit-template.txt" not in os.listdir(
        (non_default_django.project_path / ".github")
    )


def test_baked_django_with_custom_issue_template_files(cookies):
    """Test Django project has custom ISSUE templates generated correctly.

    Tests that the Custom Issue templates have had the "assignee"
    generated correctly, and post_gen deleted the standard template.
    """
    default_django = cookies.bake()

    bug_path = default_django.project_path / ".github/ISSUE_TEMPLATE/bug-report.md"
    bug_file = bug_path.read_text().splitlines()

    chore_path = default_django.project_path / ".github/ISSUE_TEMPLATE/chore.md"
    chore_file = chore_path.read_text().splitlines()

    documentation_path = (
        default_django.project_path / ".github/ISSUE_TEMPLATE/documentation-request.md"
    )
    documentation_file = documentation_path.read_text().splitlines()

    feature_path = (
        default_django.project_path / ".github/ISSUE_TEMPLATE/feature-request.md"
    )
    feature_file = feature_path.read_text().splitlines()

    assert 'assignees: "imAsparky"' in bug_file
    assert 'assignees: "imAsparky"' in chore_file
    assert 'assignees: "imAsparky"' in documentation_file
    assert 'assignees: "imAsparky"' in feature_file

    assert "ISSUE_TEMPLATE.md" not in os.listdir(
        (default_django.project_path / ".github")
    )


def test_baked_django_without_custom_issue_template_files(cookies):
    """
    Test Django project has no custom ISSUE templates generated.

    Tests that the standard template has the "project name"
    generated correctly, and post-gen deleted the Custom Issue templates.
    """
    non_default_django = cookies.bake(
        extra_context={"use_GH_custom_issue_templates": "n"}
    )

    standard_issue_path = non_default_django.project_path / ".github/ISSUE_TEMPLATE.md"
    standard_issue_file = standard_issue_path.read_text().splitlines()

    assert '- "django-boilerplate" version:' in standard_issue_file

    ISSUE_TEMPLATE_parent = non_default_django.project_path / ".github"
    dir_list = os.listdir((ISSUE_TEMPLATE_parent))
    assert "ISSUE_TEMPLATE" not in dir_list


def test_baked_django_init_file(cookies):
    """Test Django __init__.py file has been generated correctly."""
    default_django = cookies.bake()

    init_path = default_django.project_path / "django_boilerplate/__init__.py"
    init_file = init_path.read_text().splitlines()

    assert '"""Initialise django_boilerplate."""' in init_file


def test_baked_django_with_mit_license(cookies):
    """Test Django MIT license file has been generated correctly."""
    default_django = cookies.bake(
        extra_context={
            "open_source_license": "MIT license",
        }
    )

    lic_path = default_django.project_path / "LICENSE.rst"
    lic_file = lic_path.read_text().splitlines()

    assert "MIT License" in lic_file
    assert f"Copyright (c) {datetime.datetime.now().year}, Mark Sevelj" in lic_file

    assert "Apache Software License 2.0" not in lic_file
    assert "BSD License" not in lic_file
    assert "GNU GENERAL PUBLIC LICENSE" not in lic_file
    assert "ISC License" not in lic_file


def test_baked_django_with_bsd_license(cookies):
    """Test Django BSD license file has been generated correctly."""
    non_default_django = cookies.bake(
        extra_context={
            "open_source_license": "BSD license",
        }
    )

    lic_path = non_default_django.project_path / "LICENSE.rst"
    lic_file = lic_path.read_text().splitlines()

    assert "BSD License" in lic_file
    assert f"Copyright (c) {datetime.datetime.now().year}, Mark Sevelj" in lic_file

    assert "Apache Software License 2.0" not in lic_file
    assert "GNU GENERAL PUBLIC LICENSE" not in lic_file
    assert "ISC License" not in lic_file
    assert "MIT License" not in lic_file


def test_baked_django_with_isc_license(cookies):
    """Test Django ISC license file has been generated correctly."""
    non_default_django = cookies.bake(
        extra_context={
            "open_source_license": "ISC license",
        }
    )

    lic_path = non_default_django.project_path / "LICENSE.rst"
    lic_file = lic_path.read_text().splitlines()

    assert "ISC License" in lic_file
    assert f"Copyright (c) {datetime.datetime.now().year}, Mark Sevelj" in lic_file

    assert "Apache Software License 2.0" not in lic_file
    assert "BSD License" not in lic_file
    assert "GNU GENERAL PUBLIC LICENSE" not in lic_file
    assert "MIT License" not in lic_file


def test_baked_django_with_apache_license(cookies):
    """Test Django Apache Software License 2.0 license file has been generated correctly."""
    non_default_django = cookies.bake(
        extra_context={
            "open_source_license": "Apache Software License 2.0",
        }
    )

    lic_path = non_default_django.project_path / "LICENSE.rst"
    lic_file = lic_path.read_text().splitlines()

    assert "Apache Software License 2.0" in lic_file
    assert f"Copyright (c) {datetime.datetime.now().year}, Mark Sevelj" in lic_file

    assert "BSD License" not in lic_file
    assert "ISC License" not in lic_file
    assert "GNU GENERAL PUBLIC LICENSE" not in lic_file
    assert "MIT License" not in lic_file


def test_baked_django_with_gnu_license(cookies):
    """Test Django GNU General Public License v3 license file has been generated correctly."""
    non_default_django = cookies.bake(
        extra_context={
            "open_source_license": "GNU General Public License v3",
        }
    )

    lic_path = non_default_django.project_path / "LICENSE.rst"
    lic_file = lic_path.read_text().splitlines()

    assert "GNU GENERAL PUBLIC LICENSE" in lic_file
    assert f"    Copyright (C) {datetime.datetime.now().year}  Mark Sevelj" in lic_file

    assert "MIT License" not in lic_file
    assert "Apache Software License 2.0" not in lic_file
    assert "BSD License" not in lic_file
    assert "ISC License" not in lic_file


def test_baked_django_without_license(cookies):
    """Test Django  has been generated without a license file."""
    non_default_django = cookies.bake(
        extra_context={
            "open_source_license": "Not open source",
        }
    )
    assert "LICENSE.rst" not in os.listdir((non_default_django.project_path))


def test_baked_django_with_precommit_config_file(cookies):
    """Test Django pre-commit has been generated correctly."""
    default_django = cookies.bake()

    assert ".pre-commit-config.yaml" in os.listdir((default_django.project_path))


def test_baked_django_without_precommit_config_file(cookies):
    """Test Django pre-commit has not been generated."""
    non_default_django = cookies.bake(
        extra_context={
            "use_pre_commit": "n",
        }
    )

    assert ".pre-commit-config.yaml" not in os.listdir(
        (non_default_django.project_path)
    )


def test_baked_django_readme_file(cookies):
    """Test Django README file has been generated correctly."""
    default_django = cookies.bake()

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert "**Django Boilerplate**" in readme_file
    assert "*A Django project with all the boilerplate*" in readme_file


def test_baked_django_readme_with_license(cookies):
    """Test Django README file has a license type generated correctly."""
    default_django = cookies.bake()

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert ":License: MIT license" in readme_file


def test_baked_django_readme_without_license(cookies):
    """Test Django README file has no license type generated."""
    non_default_django = cookies.bake(
        extra_context={"open_source_license": "Not open source"}
    )

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert ":License: MIT license" not in readme_file
    assert ":License: BSD license" not in readme_file
    assert ":License: ISC license" not in readme_file
    assert ":License: Apache Software License 2.0" not in readme_file
    assert ":License: GNU General Public License v3" not in readme_file


def test_baked_django_readme_with_repostatus_badge(cookies):
    """Test Django README file has repo status badge generated correctly."""
    non_default_django = cookies.bake(
        extra_context={"use_repo_status_badge": "concept"}
    )

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://www.repostatus.org/badges/latest/concept.svg" in readme_file
    )
    assert "   :target: https://www.repostatus.org/#concept" in readme_file
    assert "   :alt: Project Status: Concept" in readme_file


def test_baked_django_readme_without_repostatus_badge(cookies):
    """Test Django README file has no repo status badge generated."""
    non_default_django = cookies.bake(extra_context={"use_repo_status_badge": "no"})

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://www.repostatus.org/badges/latest/concept.svg"
        not in readme_file
    )
    assert "   :target: https://www.repostatus.org/#concept" not in readme_file
    assert "   :alt: Project Status: Concept" not in readme_file


def test_baked_django_readme_with_precommit_badge(cookies):
    """Test Django README file has a pre-commit status badge generated correctly."""
    default_django = cookies.bake()

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"
        in readme_file
    )
    assert "   :target: https://github.com/pre-commit/pre-commit" in readme_file
    assert "   :alt: pre-commit" in readme_file


def test_baked_django_readme_without_precommit_badge(cookies):
    """Test Django README file has no pre-commit status badge generated."""
    non_default_django = cookies.bake(extra_context={"use_pre_commit": "n"})

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"
        not in readme_file
    )
    assert "   :target: https://github.com/pre-commit/pre-commit" not in readme_file
    assert "   :alt: pre-commit" not in readme_file


def test_baked_django_settings_file(cookies):
    """Test Django settings.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "django_boilerplate/settings.py"
    settings_file = settings_path.read_text().splitlines()

    assert '"""Django settings for django-boilerplate project.' in settings_file
    assert 'ALLOWED_HOSTS = ["www.example.com"]' in settings_file
    assert 'DEBUG = "False"' in settings_file
    assert 'ROOT_URLCONF = "django_boilerplate.urls"' in settings_file
    assert 'WSGI_APPLICATION = "django_boilerplate.wsgi.application"' in settings_file
    assert 'LANGUAGE_CODE = "en-au"' in settings_file
    assert 'LANGUAGES = "hi"' in settings_file
    assert 'TIME_ZONE = "UTC"' in settings_file
    assert 'USE_I18N = "True"' in settings_file
    assert 'USE_L10N = "True"' in settings_file


def test_baked_django_urls_file(cookies):
    """Test Django urls.py file has generated correctly."""
    default_django = cookies.bake()

    urls_path = default_django.project_path / "django_boilerplate/urls.py"
    urls_file = urls_path.read_text().splitlines()

    assert '"""django-boilerplate URL Configuration' in urls_file


def test_baked_django_wsgi_file(cookies):
    """Test Django asgi.py file has generated correctly."""
    default_django = cookies.bake()

    wsgi_path = default_django.project_path / "django_boilerplate/wsgi.py"
    wsgi_file = wsgi_path.read_text().splitlines()

    assert '"""WSGI config for django-boilerplate project.' in wsgi_file
    assert '    "DJANGO_SETTINGS_MODULE", "django_boilerplate.settings"' in wsgi_file
