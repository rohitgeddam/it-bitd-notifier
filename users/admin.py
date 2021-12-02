# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User as U

# class EmailRequiredMixin(object):
#     def __init__(self, *args, **kwargs):
#         super(EmailRequiredMixin, self).__init__(*args, **kwargs)
#         # make user email field required
#         self.fields['email'].required = True


# class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
#     pass


# class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
#     pass


# class EmailRequiredUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "fields": ("username", "email", "password1", "password2"),
#                 "classes": ("wide",),
#             },
#         ),
#     )


# admin.site.unregister(U)
admin.site.register(User)
admin.site.register(StudentProfile)
