# Create your tasks here
from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.mail import send_mass_mail
from celery import shared_task


# from django.http import HttpResponse
from twilio.rest import Client


@shared_task
def broadcast_sms(title, content):
    message_to_broadcast = f"\n{title}" f"\n{content}"
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    userlist = get_user_model().objects.all()

    recepient_list = []
    for user in userlist:

        if user.phone_number != "" and user.receive_sms_notification is True:
            phone_number = user.phone_number
            if phone_number[0] != "+":
                recepient_list.append("+91" + user.phone_number)
            else:
                recepient_list.append(user.phone_number)

    print(recepient_list)
    try:
        for recipient in recepient_list:
            if recipient:
                client.messages.create(
                    to=recipient,
                    from_=settings.TWILIO_NUMBER,
                    body=message_to_broadcast,
                )
        print("SENT SMS")
    except:
        print("ERROR OCCURED IN SENDING SMS")


@shared_task
def custom_send_email(title, content):
    userlist = get_user_model().objects.all()

    recepient_list = []

    for user in userlist:

        if user.email != "" and user.receive_email_notification is True:
            recepient_list.append(user.email)

    print("EMAIL LIST")
    print(recepient_list)

    message1 = (
        title,
        content,
        "notifier.bitd.it@gmail.com",
        recepient_list,
    )
    try:
        send_mass_mail((message1,), fail_silently=False)
        print("EMAIL SENT")
    except:
        print("ERROR OCCURED IN SENDING EMAILS")
