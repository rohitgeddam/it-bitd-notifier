# Create your tasks here
from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.mail import send_mass_mail
from celery import shared_task


# from django.http import HttpResponse
from twilio.rest import Client


@shared_task
def broadcast_sms(title, content):
    pass
    # message_to_broadcast = f"\n{title}" f"\n{content}"
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # userlist = get_user_model().objects.all()

    # recepient_list = []
    # for user in userlist:

    #     if user.phone_number != "" and user.receive_sms_notification is True:
    #         phone_number = user.phone_number
    #         if phone_number[0] != "+":
    #             recepient_list.append("+91" + user.phone_number)
    #         else:
    #             recepient_list.append(user.phone_number)

    # print(recepient_list)

    # for recipient in recepient_list:
    #     if recipient:
    #         try:
    #             client.messages.create(
    #                 to=recipient,
    #                 from_=settings.TWILIO_NUMBER,
    #                 body=message_to_broadcast,
    #             )
    #         except:
    #             print("SMS FOR " + recipient + " not sent")
                
    # print("SENT SMS")
