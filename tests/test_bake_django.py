"""django-cookiecutter test suite."""

import os


def test_django_bakes_ok_with_defaults(cookies):
    """Test cookiecutter created the django project ok."""

    default_django = cookies.bake()

    assert default_django.project_path.is_dir()
    assert default_django.exit_code == 0
    assert default_django.exception == None
    assert default_django.project_path.name == "django-boilerplate"


def test_baked_django_asgi_file(cookies):
    """Test Django asgy.py file has generated correctly."""

    default_django = cookies.bake()

    asgi_path = default_django.project_path / "django_boilerplate/asgi.py"
    asgi_file = asgi_path.read_text().splitlines()

    assert "ASGI config for django-boilerplate project." in asgi_file
    assert (
        "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_boilerplate.settings')"
        in asgi_file
    )


def test_baked_django_settings_file(cookies):
    """Test Django settings.py file has generated correctly."""

    default_django = cookies.bake()

    settings_path = default_django.project_path / "django_boilerplate/settings.py"
    settings_file = settings_path.read_text().splitlines()

    assert "Django settings for django-boilerplate project." in settings_file
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
    # assert 'DEBUG = "False"' in settings_file
    # assert 'DEBUG = "False"' in settings_file


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
    """Test Django project has no custom ISSUE templates generated.

    Tests that the standard template has the "project name"
    generated correctly, and post-gen deleted the Custom Issue templates.

    """

    default_django = cookies.bake(extra_context={"use_GH_custom_issue_templates": "n"})

    standard_issue_path = default_django.project_path / ".github/ISSUE_TEMPLATE.md"
    standard_issue_file = standard_issue_path.read_text().splitlines()

    assert '- "django-boilerplate" version:' in standard_issue_file

    ISSUE_TEMPLATE_parent = default_django.project_path / ".github"
    dir_list = os.listdir((ISSUE_TEMPLATE_parent))
    assert "ISSUE_TEMPLATE" not in dir_list


def test_baked_django_wsgi_file(cookies):
    """Test Django asgi.py file has generated correctly."""

    default_django = cookies.bake()

    wsgi_path = default_django.project_path / "django_boilerplate/wsgi.py"
    wsgi_file = wsgi_path.read_text().splitlines()

    assert "WSGI config for django-boilerplate project." in wsgi_file
    assert (
        "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_boilerplate.settings')"
        in wsgi_file
    )
