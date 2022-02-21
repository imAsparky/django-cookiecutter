"""{{cookiecutter.git_project_name}} project CustomUser Admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Customise the Admin title and header.
admin.site.site_title = "{{cookiecutter.git_project_name}}"
admin.site.site_header = "{{cookiecutter.git_project_name}} Admin"

# Require login before Admin panel is available.  Removes the opportunity for
# a brute force attack on Admin Login. Provided by django-allauth.
# https://django-allauth.readthedocs.io/en/latest/advanced.html
# Comment the following line to disable django-allauth protection.
admin.site.login = login_required(admin.site.login)


class CustomUserAdmin(UserAdmin):
    """Custom user admin."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("User Type", {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ("email",'user_type', )}),
    )

    list_display = [
        "username",
        "email",
        "user_type",
        "last_login",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    ]

    # These fields, by default, are not readonly in Admin.
    # Change to suit your needs.
    readonly_fields = [
        "date_joined",
        "last_login",
    ]

    # The Admin screen's visible items and display order.
    # Change to suit your needs.
    list_filter = ("user_type", "is_active", "is_staff", "is_superuser")

    # The Admin screen default sort order.
    # Change to suit your needs.
    ordering = (
        "username",  # Primary sort field.
        "user_type",  # Secondary sort field.
    )


# Register the custom user models.
admin.site.register(CustomUser, CustomUserAdmin)
