"""{{cookiecutter.git_project_name}} project CustomUser Tests."""

import pytest
from users.models import CustomUser as User

# Tests for the create_user function
def test_create_user_ok(new_user):
    """Test a default user is created."""

    assert new_user.username == "new_user"
    assert new_user.password != "new_userpw"  # should be a hashed password
    assert new_user.email == "new_user@newuser.com"
    assert new_user.first_name == "firstname"
    assert new_user.last_name == "lastname"
    assert new_user.user_type == "FREE"

    assert new_user.is_active
    assert not new_user.is_staff
    assert not new_user.is_superuser


def test_create_user_is_staff_ok(new_user_is_staff):
    """Test a staff user is created."""

    assert new_user_is_staff.is_staff


def test_create_user_is_superuser_ok(new_user_is_superuser):
    """Test a superuser is created."""

    assert new_user_is_superuser.is_active
    assert new_user_is_superuser.is_staff
    assert new_user_is_superuser.is_superuser


@pytest.mark.django_db
def test_create_user_errors_raised_ok():
    """Test missing new user input raises an error."""

    # Empty email.
    with pytest.raises(ValueError):
        User.objects.create_user(email="", password="new_userpw", username="new_user")

    # Empty password.
    with pytest.raises(ValueError):
        User.objects.create_user(
            email="new_user@newuser.com", password="", username="new_user"
        )


# # Tests for the create_superuser function.
def test_create_superuser_ok(new_superuser):
    """Test that a superuser is created.

    This tests the create_superuser function , used with manage.py
    """
    # User input.
    assert new_superuser.username == "new_user"
    assert new_superuser.password != "new_userpw"  # should be a hashed password
    assert new_superuser.email == "new_user@newuser.com"

    # Automatically added defaults.
    assert new_superuser.is_staff
    assert new_superuser.is_superuser
    assert new_superuser.is_active
    assert new_superuser.user_type == "SUPERUSER"


@pytest.mark.django_db
def test_create_superuser_errors_raised_ok():
    """Test that missing input for a new superuser raises an error.

    This tests the create_superuser function , used with manage.py.
    """
    # Empty email.
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="", password="new_userpw", username="new_user"
        )

    # Empty password.
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="new_user@newuser.com", password="", username="new_user"
        )

    # Is not staff.
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="new_user@newuser.com",
            password="new_userpw",
            username="new_user",
            is_staff=False,
        )

    # Is not active.
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="new_user@newuser.com",
            password="new_userpw",
            username="new_user",
            is_active=False,
        )

    # Is not superuser.
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="new_user@newuser.com",
            password="new_userpw",
            username="new_user",
            is_superuser=False,
        )
