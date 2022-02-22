"""{{cookiecutter.git_project_name}} project CustomUser Forms."""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """A basic custom user creation form."""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("user_type",)

        error_messages = {
            "username": {
                "unique": _("That user name already exists, please choose another.")
            }
        }


class CustomUserChangeForm(UserChangeForm):
    """A basic custom user change form."""

    class Meta(UserChangeForm.Meta):
        model = CustomUser
