"""{{cookiecutter.git_project_name}} project CustomUser Models."""

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """Custom user manager."""

    def create_user(
        self, email=None, password=None, **extra_fields
    ):  # pragma: no cover
        """Create and save a User."""
        """Create and save a User."""
        if not email:
            raise ValueError(_("An email address must be supplied."))
        if not password:
            raise ValueError(_("A password must be supplied."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email=None, password=None, **extra_fields
    ):  # pragma: no cover
        """Create and save a User."""
        """Create and save a SuperUser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", "SUPERUSER")

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must be staff."))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must be an active user."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must be a superuser."))
        if extra_fields.get("user_type") != "SUPERUSER":
            raise ValueError(_("Superuser must be type SUPERUSER."))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Extends the standard User model"""

    objects = CustomUserManager()

    class CustomUserType(models.TextChoices):
        """Custom user type choices"""

        # Change these to suit your needs before initial migration.
        FREE = "FREE", _("Free")
        LEVEL_1 = "LEVEL 1", _("Level 1")
        LEVEL_2 = "LEVEL 2", _("Level 2")
        STAFF = "STAFF", _("Staff")
        SUPERUSER = "SUPERUSER", _("Superuser")

    is_staff = models.BooleanField(
        _("Is Staff"),
        default=False,
        help_text="Displays if the user is currently a staff member.",
    )
    is_active = models.BooleanField(
        _("Is Active"),
        default=True,
        help_text="Displays if the user is currently an active user.",
    )
    date_joined = models.DateTimeField(
        _("Date Joined"),
        default=timezone.now,
        help_text="Displays the user join date.",
    )
    email = models.EmailField(
        _("Email Address"),
        unique=True,
        max_length=255,
        help_text="Displays if the user email address",
    )
    user_type = models.CharField(
        _("Type"),
        null=False,
        blank=False,
        max_length=50,
        choices=CustomUserType.choices,
        default=CustomUserType.FREE,
        help_text="Displays the users current user type.",
    )

    def __str__(self):
        return self.username
