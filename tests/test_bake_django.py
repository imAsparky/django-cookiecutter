"""django-cookiecutter test suite."""


def test_django_bakes_ok_with_defaults(cookies):
    """Test cookiecutter created the django project ok."""

    default_django = cookies.bake()

    assert default_django.project_path.is_dir()
    assert default_django.exit_code == 0
    assert default_django.exception == None
    assert default_django.project_path.name == "django-boilerplate"


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


def test_baked_django_urls_file(cookies):
    """Test Django urls.py file has generated correctly."""

    default_django = cookies.bake()

    urls_path = default_django.project_path / "django_boilerplate/urls.py"
    urls_file = urls_path.read_text().splitlines()

    assert '"""django-boilerplate URL Configuration' in urls_file
    # assert 'DEBUG = "False"' in settings_file
    # assert 'DEBUG = "False"' in settings_file


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
