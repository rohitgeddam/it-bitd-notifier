# Register your models here.
from .models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User as U

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "password", "batch")}),
        (
            "Contact",
            {
                "fields": (
                    "email",
                    "phone_number",
                )
            },
        ),
        (
            "Settings",
            {
                "fields": (
                    "receive_email_notification",
                    "receive_sms_notification",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "phone_number",
                    "batch",
                    "receive_email_notification",
                    "receive_sms_notification",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
