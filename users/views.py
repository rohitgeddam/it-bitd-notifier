from django.shortcuts import render
from .models import StudentProfile

# Create your views here.
def user_profile_view(request):
    """User profile view"""
    context = {}
    if request.user and request.user.is_authenticated:
        context["user"] = request.user
        context["profile"] = StudentProfile.objects.get(user=request.user)
    return render(request, "users/profile.html", context)
