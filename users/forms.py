from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class SettingsChangeForm(forms.Form):
    receive_email_notification = forms.BooleanField(required=False)
    receive_sms_notification = forms.BooleanField(required=False)
