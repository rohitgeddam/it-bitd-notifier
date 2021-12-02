from django.db import models
from core.models import YearTag

from django.core.mail import send_mass_mail
from django.conf import settings

# from django.http import HttpResponse
from twilio.rest import Client


def broadcast_sms(self):
    message_to_broadcast = f"{self.title}" f"{self.content}"
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(
                to=recipient, from_=settings.TWILIO_NUMBER, body=message_to_broadcast
            )


def custom_send_email(self):
    recepient_list = ["vrahul200023@gmail.com", "rohitgeddam2018@gmail.com"]
    message1 = (
        self.title,
        self.content,
        "notifier.it.bitd@gmail.com",
        recepient_list,
    )
    send_mass_mail((message1,), fail_silently=False)


class NoticeFile(models.Model):
    """Class for Notice Files"""

    file = models.FileField(upload_to="uploads/files", blank=True, null=True)
    notice = models.ForeignKey("Notice", on_delete=models.CASCADE)


# Create your models here.
class Notice(models.Model):
    """Class for Notice"""

    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(YearTag, related_name="notices")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        custom_send_email(self)
        broadcast_sms(self)
        return super().save(*args, **kwargs)
