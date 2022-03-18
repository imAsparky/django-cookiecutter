"""django-cookiecutter test suite."""

import datetime
import os

from test_helper import bake_checker

current_year = datetime.datetime.now().year


def test_django_bakes_ok_with_defaults(cookies):
    """Test cookiecutter created the Django project ok."""

    default_django = cookies.bake()

    assert default_django.exit_code == 0
    assert default_django.project_path.is_dir()
    assert default_django.exception == None  # noqa: E711
    assert default_django.project_path.name == "django-boilerplate"


def test_baked_django_core_asgi_file_ok(cookies):
    """Test Django Core asgi.py file has been generated correctly."""
    default_django = cookies.bake()

    asgi_path = default_django.project_path / "core/asgi.py"
    asgi_file = asgi_path.read_text().splitlines()

    assert '"""django-boilerplate ASGI Configuration.' in asgi_file
    assert (
        'os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")'
        in asgi_file
    )


def test_baked_django_core_init_py_file(cookies):
    """Test Django Core __init__.py file has been generated correctly."""
    default_django = cookies.bake()

    init_path = default_django.project_path / "core/__init__.py"
    init_file = init_path.read_text().splitlines()

    assert '"""Initialise django-boilerplate Core App."""' in init_file


def test_baked_django_core_urls_file_ok(cookies):
    """Test Django Core urls.py file has generated correctly."""
    default_django = cookies.bake()

    urls_path = default_django.project_path / "core/urls.py"
    urls_file = urls_path.read_text().splitlines()

    assert '"""django-boilerplate URL Configuration.' in urls_file


def test_baked_django_core_wsgi_file_ok(cookies):
    """Test Django Core wsgi.py file has generated correctly."""
    default_django = cookies.bake()

    wsgi_path = default_django.project_path / "core/wsgi.py"
    wsgi_file = wsgi_path.read_text().splitlines()

    assert '"""django-boilerplate WSGI Configuration.' in wsgi_file
    assert (
        'os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")'
        in wsgi_file
    )


def test_baked_django_core_views_init_py_file(cookies):
    """Test Django Core Views __init__.py file has been generated correctly."""
    default_django = cookies.bake()

    init_path = default_django.project_path / "core/views/__init__.py"
    init_file = init_path.read_text().splitlines()

    assert '"""Initialise django-boilerplate Core App Views."""' in init_file


def test_baked_django_core_views_generic_init_py_file(cookies):
    """Test Django Core Views Generic __init__.py file has been generated correctly."""
    default_django = cookies.bake()

    init_path = default_django.project_path / "core/views/generic/__init__.py"
    init_file = init_path.read_text().splitlines()

    assert '"""Initialise django-boilerplate Core App Generic Views."""' in init_file


def test_baked_django_core_views_generic_base_py_file(cookies):
    """Test Django Core Views Generic base.py file has been generated correctly."""
    default_django = cookies.bake()

    base_path = default_django.project_path / "core/views/generic/base.py"
    base_file = base_path.read_text().splitlines()

    assert '"""django-boilerplate Core App Generic Views Base."""' in base_file


def test_baked_django_core_views_generic_base_py_copyright_license(cookies):
    """Test Django Core Views Generic base.py file has been generated correctly."""
    default_django = cookies.bake()

    base_path = default_django.project_path / "core/views/generic/base.py"
    base_file = base_path.read_text().splitlines()

    assert "    Copyright (c) 2021 Pablo Rivera" in base_file


def test_baked_django_core_views_generic_detail_py_file(cookies):
    """Test Django Core Views Generic detail.py file has been generated correctly."""
    default_django = cookies.bake()

    detail_path = default_django.project_path / "core/views/generic/detail.py"
    detail_file = detail_path.read_text().splitlines()

    assert '"""django-boilerplate Core App Generic Views Detail."""' in detail_file


def test_baked_django_core_views_generic_edit_py_file(cookies):
    """Test Django Core Views Generic edit.py file has been generated correctly."""
    default_django = cookies.bake()

    edit_path = default_django.project_path / "core/views/generic/edit.py"
    edit_file = edit_path.read_text().splitlines()

    assert '"""django-boilerplate Core App Generic Views Edit."""' in edit_file


def test_baked_django_core_views_generic_list_py_file(cookies):
    """Test Django Core Views Generic list.py file has been generated correctly."""
    default_django = cookies.bake()

    list_path = default_django.project_path / "core/views/generic/list.py"
    list_file = list_path.read_text().splitlines()

    assert '"""django-boilerplate Core App Generic Views List."""' in list_file


def test_baked_django_custom_admin_file_ok(cookies):
    """Test Django custom users/admin.py file has been generated correctly."""
    default_django = cookies.bake()

    admin_path = default_django.project_path / "users/admin.py"
    admin_file = str(admin_path.read_text().splitlines())

    assert 'admin.site.site_title = "django-boilerplate"' in admin_file
    assert 'admin.site.site_header = "django-boilerplate Admin"' in admin_file


def test_baked_django_docs_with_code_of_conduct(cookies):
    """Test Django docs code of conduct file has been generated correctly."""
    default_django = cookies.bake()

    assert "code-of-conduct.rst" in os.listdir(
        default_django.project_path / "docs/source"
    )


def test_baked_django_docs_without_code_of_conduct(cookies):
    """Test Django docs code of conduct file has not been generated."""
    non_default_django = cookies.bake(
        extra_context={"include_contributor_covenant_code_of_conduct": "n"}
    )

    assert "code-of-conduct.rst" not in os.listdir(
        non_default_django.project_path / "docs/source"
    )


def test_baked_django_with_commit_message_file(cookies):
    """Test Django Conventional commit message template has been generated correctly."""
    default_django = cookies.bake()

    assert ".git-commit-template.txt" in os.listdir(
        default_django.project_path / ".github"
    )


def test_baked_django_without_commit_message_file(cookies):
    """Test Django Conventional commit message template has not been generated."""
    non_default_django = cookies.bake(
        extra_context={
            "create_conventional_commits_edit_message": "n",
        }
    )

    assert ".git-commit-template.txt" not in os.listdir(
        non_default_django.project_path / ".github"
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
        default_django.project_path / ".github"
    )


def test_baked_django_without_custom_issue_template_files(cookies):
    """Test Django project has no custom ISSUE templates generated.

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
    dir_list = os.listdir(ISSUE_TEMPLATE_parent)
    assert "ISSUE_TEMPLATE" not in dir_list


def test_baked_django_with_docker(cookies):
    """Test Django Docker folder has been generated correctly."""
    non_default_django = cookies.bake(extra_context={"deploy_with_docker": "y"})

    assert "Dockerfile" in os.listdir(non_default_django.project_path)
    assert ".dockerignore" in os.listdir(non_default_django.project_path)
    assert "docker-compose-swarm.yml" in os.listdir(
        non_default_django.project_path / "compose"
    )
    assert "docker-entrypoint.sh" in os.listdir(non_default_django.project_path)


def test_baked_django_without_docker(cookies):
    """Test Django Docker folder has not been generated."""
    default_django = cookies.bake()

    assert "Dockerfile" not in os.listdir(default_django.project_path)
    assert ".dockerignore" not in os.listdir(default_django.project_path)

    assert "compose" not in os.listdir(default_django.project_path)
    assert "docker-entrypoint.sh" not in os.listdir(default_django.project_path)


def test_baked_django_with_docs(cookies):
    """Test Django docs folder has been generated correctly."""
    default_django = cookies.bake()

    assert "docs" in os.listdir(default_django.project_path)

    requirements_path = default_django.project_path / "requirements_dev.txt"
    requirements_file = str(requirements_path.read_text().splitlines())

    assert "-r docs/requirements.txt" in requirements_file

    tox_path = default_django.project_path / "tox.ini"
    tox_file = str(tox_path.read_text().splitlines())

    assert "[testenv:docs]" in tox_file


def test_baked_django_without_docs(cookies):
    """Test Django docs folder has not been generated."""
    non_default_django = cookies.bake(extra_context={"include_sphinx_docs": "n"})

    assert "docs" not in os.listdir(non_default_django.project_path)

    requirements_path = non_default_django.project_path / "requirements_dev.txt"
    requirements_file = str(requirements_path.read_text().splitlines())

    assert "-r docs/requirements.txt" not in requirements_file

    tox_path = non_default_django.project_path / "tox.ini"
    tox_file = str(tox_path.read_text().splitlines())

    assert "[testenv:docs]" not in tox_file


def test_baked_django_with_docs_conf_settings_ok(cookies):
    """Test Sphinx conf.py has been generated correctly."""
    default_django = cookies.bake()

    conf_path = default_django.project_path / "docs/source/conf.py"
    conf_file = str(conf_path.read_text().splitlines())

    assert (
        '"""Django Boilerplate documentation Sphinx build configuration file."""'
        in conf_file
    )
    assert '__version__ = "0.1.0"' in conf_file
    assert 'project = "Django Boilerplate"' in conf_file
    assert f'copyright = "{current_year}, Mark Sevelj"' in conf_file
    assert 'author = "Mark Sevelj"' in conf_file


def test_baked_django_docs_with_discussion_index(cookies):
    """Test Django docs discussion index template file has been generated correctly."""
    default_django = cookies.bake()

    index_path = (
        default_django.project_path / "docs/source/discussion/index-discussion.rst"
    )
    index_file = index_path.read_text().splitlines()

    assert (
        "See below for a list of discussion material for Django Boilerplate."
        in index_file
    )


def test_baked_django_docs_with_how_to_contribute(cookies):
    """Test Django docs how-to contribute template file has been generated correctly."""
    default_django = cookies.bake()

    contrib_path = (
        default_django.project_path / "docs/source/how-tos/how-to-contribute.rst"
    )
    contrib_file = contrib_path.read_text().splitlines()

    assert (
        ".. _bug: https://github.com/imAsparky/django-boilerplate/issues"
        in contrib_file
    )
    assert "Look through Django Boilerplate GitHub issues_ for bugs." in contrib_file
    assert (
        "Look through Django Boilerplate GitHub issues_ for features." in contrib_file
    )
    assert (
        "Django Boilerplate strives to have excellent documentation for several reasons:"
        in contrib_file
    )
    assert (
        "Django Boilerplate provides the four pillars Tutorials, How-to, Reference and"
        in contrib_file
    )
    assert (
        "Django Boilerplate uses Sphinx to document the API.  Class's, modules, or"
        in contrib_file
    )
    assert (
        "an `Issue <https://github.com/imAsparky/django-boilerplate/issues>`_."
        in contrib_file
    )
    assert (
        "Here's how to set up `django-boilerplate` for local development. We have"
        in contrib_file
    )
    assert (
        "2. From your GitHub account, fork the `django-boilerplate` repository."
        in contrib_file
    )
    assert "    Django Boilerplate uses python-semantic-release." in contrib_file
    assert (
        ".. _issues: https://github.com/imAsparky/django-boilerplate/issues"
        in contrib_file
    )


def test_baked_django_docs_without_how_to_contribute(cookies):
    """Test Django docs how-to contribute template file has not been generated."""
    non_default_django = cookies.bake(
        extra_context={"include_how_to_contribute_template": "n"}
    )

    assert "how-to-contribute.rst" not in os.listdir(
        non_default_django.project_path / "docs/source/how-tos"
    )


def test_baked_django_docs_with_how_to_index(cookies):
    """Test Django docs how-to index template file has been generated correctly."""
    default_django = cookies.bake()

    index_path = default_django.project_path / "docs/source/how-tos/index-how-to.rst"
    index_file = index_path.read_text().splitlines()

    assert "See below for a list of How-To for Django Boilerplate." in index_file


def test_baked_django_docs_with_templates(cookies):
    """Test Django docs templates folder has been generated correctly."""
    default_django = cookies.bake()

    assert "doc-templates" in os.listdir(default_django.project_path / "docs/source")


def test_baked_django_docs_without_templates(cookies):
    """Test Django docs templates folder has not been generated."""
    non_default_django = cookies.bake(
        extra_context={"include_documentation_templates": "n"}
    )

    assert "doc-templates" not in os.listdir(
        non_default_django.project_path / "docs/source"
    )


def test_baked_django_docs_with_references_index(cookies):
    """Test Django docs reference index template file has been generated correctly."""
    default_django = cookies.bake()

    index_path = (
        default_django.project_path / "docs/source/reference/index-reference.rst"
    )
    index_file = index_path.read_text().splitlines()

    assert (
        "See below for a list of reference material for Django Boilerplate."
        in index_file
    )


def test_baked_django_docs_templates_index(cookies):
    """Test Django docs index template file has been generated correctly."""
    default_django = cookies.bake()

    index_path = (
        default_django.project_path / "docs/source/doc-templates/index-templates.rst"
    )
    index_file = index_path.read_text().splitlines()

    assert "A list of document templates for Django Boilerplate." in index_file


def test_baked_django_with_git_initiated(cookies):
    """Test Django git init has generated correctly."""
    default_django = cookies.bake()

    assert ".git" in os.listdir(default_django.project_path)

    git_remote = bake_checker(
        "git",
        "remote",
        "-v",
        cwd=default_django.project_path,
    )

    assert "git@github.com:imAsparky/django-boilerplate.git (fetch)" in git_remote


def test_baked_django_without_git_initiated(cookies):
    """Test Django git init has not generated."""
    non_default_django = cookies.bake(
        extra_context={"automatic_set_up_git_and_initial_commit": "n"}
    )

    assert ".git" not in os.listdir(non_default_django.project_path)


def test_baked_django_with_github_action_test_workflow(cookies):
    """Test Django GitHub test action file has generated correctly."""
    default_django = cookies.bake()

    assert "test_contribution.yaml" in os.listdir(
        default_django.project_path / ".github/workflows"
    )


def test_baked_django_without_github_action_test_workflow(cookies):
    """Test Django GitHub test action file has not generated."""
    non_default_django = cookies.bake(
        extra_context={"create_repo_auto_test_workflow": "n"}
    )

    assert "test_contribution.yaml" not in os.listdir(
        non_default_django.project_path / ".github/workflows"
    )


def test_baked_django_with_license_mit(cookies):
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


def test_baked_django_with_license_bsd(cookies):
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


def test_baked_django_with_license_isc(cookies):
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


def test_baked_django_with_license_apache(cookies):
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


def test_baked_django_with_license_gnu(cookies):
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
    assert "LICENSE.rst" not in os.listdir(non_default_django.project_path)


def test_baked_django_with_precommit_config_file(cookies):
    """Test Django pre-commit has been generated correctly."""
    default_django = cookies.bake()

    assert ".pre-commit-config.yaml" in os.listdir(default_django.project_path)


def test_baked_django_without_precommit_config_file(cookies):
    """Test Django pre-commit has not been generated."""
    non_default_django = cookies.bake(
        extra_context={
            "use_pre_commit": "n",
        }
    )

    assert ".pre-commit-config.yaml" not in os.listdir(non_default_django.project_path)


def test_baked_django_with_pyup_io(cookies):
    """Test Django pyup.io file has been generated correctly."""
    default_django = cookies.bake()

    assert ".pyup.yml" in os.listdir(default_django.project_path)

    pyup_path = default_django.project_path / ".pyup.yml"
    pyup_file = pyup_path.read_text().splitlines()

    assert "  - imAsparky" in pyup_file

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://pyup.io/repos/github/imAsparky/django-boilerplate/shield.svg"
        in readme_file
    )
    assert (
        "   :target: https://pyup.io/repos/github/imAsparky/django-boilerplate/"
        in readme_file
    )
    assert "   :alt: Updates" in readme_file


def test_baked_django_without_pyup_io(cookies):
    """Test Django pyup.io file has not been generated."""
    non_default_django = cookies.bake(extra_context={"use_pyup_io": "n"})

    assert ".pyup.yml" not in os.listdir(non_default_django.project_path)

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://pyup.io/repos/github/imAsparky/django-boilerplate/shield.svg"
        not in readme_file
    )
    assert (
        "   :target: https://pyup.io/repos/github/imAsparky/django-boilerplate/"
        not in readme_file
    )
    assert "   :alt: Updates" not in readme_file


def test_baked_django_readme_file(cookies):
    """Test Django README file has been generated correctly."""
    default_django = cookies.bake()

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert "**Django Boilerplate**" in readme_file
    assert "*A Django project with all the boilerplate*" in readme_file
    assert '**Version = "0.1.0"**' in readme_file


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
    assert "   :alt: Project Status: concept" in readme_file


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


def test_baked_django_with_read_the_docs(cookies):
    """Test Django readthedocs config has been generated correctly."""
    default_django = cookies.bake()

    assert ".readthedocs.yaml" in os.listdir(default_django.project_path)

    rtd_path = default_django.project_path / "README.rst"
    rtd_file = rtd_path.read_text().splitlines()

    assert (
        ".. image:: https://readthedocs.org/projects/django-boilerplate/badge/?version=latest"
        in rtd_file
    )
    assert (
        "   :target: https://django-boilerplate.readthedocs.io/en/latest/?badge=latest"
        in rtd_file
    )
    assert "   :alt: Documentation Status" in rtd_file


def test_baked_django_without_read_the_docs(cookies):
    """Test Django readthedocs config has not been generated correctly."""
    non_default_django = cookies.bake(
        extra_context={
            "use_readthedocs": "n",
        }
    )

    assert ".readthedocs.yaml" not in os.listdir(non_default_django.project_path)

    rtd_path = non_default_django.project_path / "README.rst"
    rtd_file = rtd_path.read_text().splitlines()

    assert (
        ".. image:: https://readthedocs.org/projects/django-boilerplate/badge/?version=latest"
        not in rtd_file
    )
    assert (
        "   :target: https://django-boilerplate.readthedocs.io/en/latest/?badge=latest"
        not in rtd_file
    )
    assert "   :alt: Documentation Status" not in rtd_file


def test_baked_django_with_semantic_release(cookies):
    """Test Django semantic-release file has been generated correctly."""
    default_django = cookies.bake()

    assert "CHANGELOG.md" in os.listdir(default_django.project_path)
    assert "semantic.yaml" in os.listdir(default_django.project_path / ".github")
    assert "semantic_release.yaml" in os.listdir(
        default_django.project_path / ".github/workflows"
    )

    readme_path = default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg"
        in readme_file
    )
    assert (
        "   :target: https://python-semantic-release.readthedocs.io/en/latest/"
        in readme_file
    )
    assert "   :alt: Python Sementic Release" in readme_file


def test_baked_django_without_semantic_release(cookies):
    """Test Django semantic-release file has not been generated."""
    non_default_django = cookies.bake(
        extra_context={"use_GH_action_semantic_version": "n"}
    )

    assert "CHANGELOG.md" not in os.listdir(non_default_django.project_path)
    assert "semantic.yaml" not in os.listdir(
        non_default_django.project_path / ".github"
    )
    assert "semantic_release.yaml" not in os.listdir(
        non_default_django.project_path / ".github/workflows"
    )

    readme_path = non_default_django.project_path / "README.rst"
    readme_file = readme_path.read_text().splitlines()

    assert (
        ".. image:: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg"
        not in readme_file
    )
    assert (
        "   :target: https://python-semantic-release.readthedocs.io/en/latest/"
        not in readme_file
    )
    assert "   :alt: Python Sementic Release" not in readme_file


def test_baked_django_base_settings_base_file_ok(cookies):
    """Test Django config/settings/base.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "config/settings/base.py"

    settings_file = settings_path.read_text().splitlines()

    assert '"""Django base settings for django-boilerplate project.' in settings_file
    assert 'ROOT_URLCONF = "core.urls"' in settings_file
    assert 'WSGI_APPLICATION = "core.wsgi.application"' in settings_file
    assert 'LANGUAGE_CODE = "en"' in settings_file
    assert '    ("en", _("English")),' in settings_file
    assert 'TIME_ZONE = "UTC"' in settings_file
    assert "USE_I18N = True" in settings_file


def test_baked_django_settings_local_file_ok(cookies):
    """Test Django config/settings/local.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "config/settings/local.py"
    settings_file = settings_path.read_text().splitlines()

    assert (
        '"""Django local settings for django-boilerplate project."""' in settings_file
    )


def test_baked_django_settings_production_file_ok(cookies):
    """Test Django config/settings/production.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "config/settings/production.py"
    settings_file = settings_path.read_text().splitlines()

    assert (
        '"""Django production settings for django-boilerplate project."""'
        in settings_file
    )
    assert 'ALLOWED_HOSTS = [""]' in settings_file


def test_baked_django_settings_staging_file_ok(cookies):
    """Test Django config/settings/staging.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "config/settings/staging.py"
    settings_file = settings_path.read_text().splitlines()

    assert (
        '"""Django staging settings for django-boilerplate project."""' in settings_file
    )
    assert 'ALLOWED_HOSTS = [""]' in settings_file


def test_baked_django_settings_test_file_ok(cookies):
    """Test Django config/settings/test.py file has generated correctly."""
    default_django = cookies.bake()

    settings_path = default_django.project_path / "config/settings/test.py"
    settings_file = settings_path.read_text().splitlines()

    assert '"""Django test settings for django-boilerplate project."""' in settings_file
    assert 'ALLOWED_HOSTS = [""]' in settings_file


def test_baked_django_tox_file_ok(cookies):
    """Test Django tox.ini file has been generated correctly."""
    default_django = cookies.bake()

    tox_path = default_django.project_path / "tox.ini"
    tox_file = str(tox_path.read_text().splitlines())

    assert '  find {toxinidir}/core -type f -name "*.pyc" -delete' in tox_file
    assert "mypy --ignore-missing-imports {toxinidir}/core" in tox_file
