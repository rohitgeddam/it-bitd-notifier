from django.db import models
from ckeditor.fields import RichTextField


class EventPhoto(models.Model):
    """class for Event Photos"""

    photo = models.ImageField(upload_to="uploads/events/images")
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


class EventFile(models.Model):
    """class for event files"""

    file = models.FileField(upload_to="uploads/events/files")
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


# Create your models here.
class Event(models.Model):
    """Class for Event"""

    title = models.CharField(max_length=64)
    description = RichTextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.date}"

    def save(self, *args, **kwargs):

        return super().save(*args, **kwargs)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.html import strip_tags

# from .tasks import custom_send_email, broadcast_sms
from shared.send_push_notification import bulk_send_push_messages
from shared.send_emails import custom_send_email
from shared.send_sms import broadcast_sms

@receiver(post_save, sender=Event)
def my_handler(sender, instance, **kwargs):
    print("post save callback")
    print(instance.id)
    full_url = f"{settings.BASE_URL}/events/{instance.id}"
    content = f"\n{strip_tags(instance.description)}\nDate - {instance.date}\nTime - {instance.time}\nView Event - {full_url}"
    bulk_send_push_messages.delay({"title": "New Event", "body": instance.title })
    custom_send_email.delay(instance.title, content)
    broadcast_sms.delay(instance.title, content)
