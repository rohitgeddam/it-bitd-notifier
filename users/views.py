from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SettingsChangeForm
from django.urls import reverse

# Create your views here.
def user_profile_view(request):
    """User profile view"""
    context = {}
    if request.user and request.user.is_authenticated:
        context["user"] = request.user
        # context["profile"] = StudentProfile.objects.get(user=request.user)
    return render(request, "users/profile.html", context)


def change_settings(request):
    """User change settings"""
    user = request.user

    if request.method == "POST":

        form = SettingsChangeForm(request.POST)

        if form.is_valid():
            user.receive_email_notification = form.cleaned_data[
                "receive_email_notification"
            ]
            user.receive_sms_notification = form.cleaned_data[
                "receive_sms_notification"
            ]

            user.save()

            return HttpResponseRedirect(reverse("profile"))

    else:
        form = SettingsChangeForm(
            {
                "receive_email_notification": user.receive_email_notification,
                "receive_sms_notification": user.receive_sms_notification,
            }
        )

    return render(request, "users/settings_change.html", {"form": form})
