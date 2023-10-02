"""{{cookiecutter.git_project_name}} Test Fixtures."""

import pytest
from django.contrib.auth import get_user_model
from django.test.utils import override_settings

User = get_user_model()


# This settings snippet is from Speed Up Your Django Tests
# please support by purchasing from here https://adamchainz.gumroad.com/l/suydt
@pytest.fixture(scope="session", autouse=True)
def test_settings():
    """Provide settings override for tests"""
    with override_settings(**TEST_SETTINGS):
        yield


TEST_SETTINGS = {
    "PAGINATION_COUNT": 10,
}


# Fixtures for create_user function.
@pytest.fixture
def new_user_factory(db):
    """Factory for create_user function."""

    def create_user(
        username: str = "new_user",
        password: str = "new_userpw",
        email: str = "new_user@newuser.com",
        first_name: str = "firstname",
        last_name: str = "lastname",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
        user_type: str = "FREE",
    ):
        """Return a new user with default values."""
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            user_type=user_type,
        )
        return user

    return create_user


@pytest.fixture
def new_user(db, new_user_factory):
    """Return a default new user"""
    return new_user_factory()


@pytest.fixture
def new_user_is_staff(db, new_user_factory):
    """Return a new staff user"""
    return new_user_factory(is_staff=True)


@pytest.fixture
def new_user_is_superuser(db, new_user_factory):
    """Return a new superuser"""
    return new_user_factory(is_staff=True, is_active=True, is_superuser=True)


# Fixtures for create_superuser function.
@pytest.fixture
def new_superuser_factory(db):
    """Factory for create_superuser function."""

    def create_superuser(
        username: str = "new_user",
        password: str = "new_userpw",
        email: str = "new_user@newuser.com",
    ):
        """Return a new superuser with default values."""
        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )
        return user

    return create_superuser


@pytest.fixture
def new_superuser(db, new_superuser_factory):
    """Return a new superuser"""
    return new_superuser_factory()
