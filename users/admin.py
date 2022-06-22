# Register your models here.
from .models import User, PushNotificationToken
from django.urls import path

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User as U

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.contrib import messages

from io import TextIOWrapper


class CustomUserAdmin(UserAdmin):
    change_list_template = "users/users_changelist.html"

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

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("download-user-list/", self.download_user_list),
            path("upload-user-list/", self.upload_user_list),
        ]
        return my_urls + urls

    def download_user_list(self, request):
        userlist = self.model.objects.all()
        print(userlist)
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="user-list.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ["username", "email", "phone_number", "batch", "first name", "last name"]
        )
        for user in userlist:
            writer.writerow(
                [
                    user.username,
                    user.email,
                    user.phone_number,
                    user.batch,
                    user.first_name,
                    user.last_name,
                ]
            )
        self.message_user(request, "downloading user list")

        return response

    def upload_user_list(self, request):
        if request.method == "POST":
            csv_file = TextIOWrapper(
                request.FILES["csv_file"].file, encoding="ascii", errors="replace"
            )

            reader = csv.reader(csv_file)
            idx = 0

            failed = False

            for row in reader:
                if idx == 0:
                    idx = idx + 1
                    continue
                idx = idx + 1
                username = row[0]
                email = row[1]
                phone_number = row[2]
                batch = row[3]
                f_name = row[4]
                l_name = row[5]
                if len(self.model.objects.filter(username=username)) == 0:
                    try:
                        u = self.model(
                            username=username,
                            email=email,
                            phone_number=phone_number,
                            batch=batch,
                            first_name=f_name,
                            last_name=l_name,
                        )
                        u.set_password(username)
                        u.save()
                    except:
                        failed = True

                else:
                    continue

            if failed:
                self.message_user(
                    request,
                    "There was an error at row "
                    + str(idx)
                    + "  please correct the format and upload again.",
                    level=messages.ERROR,
                )
            else:
                self.message_user(request, "User List Upload Successful")

        return HttpResponseRedirect("../")


# class EmailRequiredMixin(object):
#     def __init__(self, *args, **kwargs):
#         super(EmailRequiredMixin, self).__init__(*args, **kwargs)
#         # make user email field required
#         self.fields["email"].required = True


# class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
#     pass


# class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
#     pass


# class EmailRequiredUserAdmin(UserAdmin):
#     change_list_template = "users/users_changelist.html"

#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "username",
#                     "password1",
#                     "password2",
#                     "email",
#                     "phone_number",
#                     "batch",
#                     "receive_email_notification",
#                     "receive_sms_notification",
#                     "is_staff",
#                     "is_active",
#                 ),
#             },
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)

# def get_urls(self):
#     urls = super().get_urls()
#     my_urls = [
#         path('download-user-list/', self.download_user_list),
#         path('upload-user-list/', self.upload_user_list),
#     ]
#     return my_urls + urls

# def download_user_list(self, request):
#     userlist = self.model.objects.all()
#     print(userlist)
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="user-list.csv"'
#     writer = csv.writer(response)
#     writer.writerow(["username", "email", "phone_number", "batch", "first name", "last name"])
#     for user in userlist:
#         writer.writerow([user.username, user.email, user.phone_number, user.batch, user.first_name, user.last_name])
#     self.message_user(request, "downloading user list")

#     return response


# def upload_user_list(self, request):
#     if request.method == "POST":
#         csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='ascii', errors='replace')

#         reader = csv.reader(csv_file)
#         idx = 0

#         failed = False

#         for row in reader:
#             if idx == 0:
#                 idx = idx + 1
#                 continue
#             idx = idx + 1
#             username = row[0]
#             email = row[1]
#             phone_number = row[2]
#             batch = row[3]
#             f_name = row[4]
#             l_name = row[5]
#             if(len(self.model.objects.filter(username=username)) == 0):
#                 try:
#                     u = self.model(username=username, email=email, phone_number=phone_number, batch=batch, first_name=f_name, last_name=l_name)
#                     u.set_password(username)
#                     u.save()
#                 except:
#                     failed = True

#             else:
#                 continue

#         if failed:
#             self.message_user(request, "There was an error at row " + str(idx) + "  please correct the format and upload again." , level=messages.ERROR)
#         else:
#             self.message_user(request, "User List Upload Successful")

#     return HttpResponseRedirect("../")


admin.site.register(User, CustomUserAdmin)
# admin.site.register(User, EmailRequiredUserAdmin)
admin.site.register(PushNotificationToken)