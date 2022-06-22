# Create your tasks here
from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.mail import send_mass_mail
from celery import shared_task


# from django.http import HttpResponse
from twilio.rest import Client



@shared_task
def custom_send_email(title, content):
    pass
#     userlist = get_user_model().objects.all()

#     recepient_list = []

#     for user in userlist:

#         if user.email != "" and user.receive_email_notification is True:
#             recepient_list.append(user.email)

#     message1 = (
#         title,
#         content,
#         "notifier.bitd.it@gmail.com",
#         recepient_list,
#     )
# # try:
#     send_mass_mail((message1,), fail_silently=False)
#     print("EMAIL SENT")
    # except:
        # print("ERROR OCCURED IN SENDING EMAILS")