"""{{cookiecutter.git_project_name}} project CustomUser Models."""

from django.apps import apps
from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, username, email, password, **extra_fields
    ):  # pragma: no cover
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("A username must be supplied.")
        email = self.normalize_email(email)
        if not email:
            raise ValueError(_("An email address must be supplied."))
        if not password:
            raise ValueError(_("A password must be supplied."))
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self, username, email=None, password=None, **extra_fields
    ):  # pragma: no cover
        """
        Create and save a standard user with the supplied username, email, and password.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(
        self, username, email=None, password=None, **extra_fields
    ):  # pragma: no cover
        """
        Create and save a super user with the supplied username, email, and password.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", "SUPERUSER")

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must be staff."))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must be an active user."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must be a superuser."))
        if extra_fields.get("user_type") != "SUPERUSER":
            raise ValueError(_("Superuser must be type SUPERUSER."))

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(
        self,
        perm,
        is_active=True,
        include_superusers=True,
        backend=None,
        obj=None,
    ):  # pragma: no cover
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


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

    user_type = models.CharField(
        _("Type"),
        null=False,
        blank=False,
        max_length=50,
        choices=CustomUserType.choices,
        default=CustomUserType.FREE,
        help_text="Displays the users current user type.",
    )
