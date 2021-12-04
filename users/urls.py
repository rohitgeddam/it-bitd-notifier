from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.user_profile_view, name="profile"),
    path("settings/change", views.change_settings, name="settings_change"),
]
