# Create your tasks here
from django.conf import settings

from django.core.mail import send_mass_mail
from celery import shared_task


# from django.http import HttpResponse
from twilio.rest import Client


@shared_task
def broadcast_sms(title, content):
    message_to_broadcast = f"{title}" f"{content}"
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
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
    recepient_list = ["vrahul200023@gmail.com", "rohitgeddam2018@gmail.com"]
    message1 = (
        title,
        content,
        "notifier.it.bitd@gmail.com",
        recepient_list,
    )
    try:
        send_mass_mail((message1,), fail_silently=False)
        print("EMAIL SENT")
    except:
        print("ERROR OCCURED IN SENDING EMAILS")
