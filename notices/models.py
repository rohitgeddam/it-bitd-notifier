from django.db import models
from core.models import YearTag
from ckeditor.fields import RichTextField

# from notices.tasks import broadcast_sms, custom_send_email


class NoticeFile(models.Model):
    """Class for Notice Files"""

    file = models.FileField(upload_to="uploads/files", blank=True, null=True)
    notice = models.ForeignKey("Notice", on_delete=models.CASCADE)


# Create your models here.
class Notice(models.Model):
    """Class for Notice"""

    title = models.CharField(max_length=256)
    content = RichTextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(YearTag, related_name="notices")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        return super().save(*args, **kwargs)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from django.utils.html import strip_tags
from shared.send_push_notification import bulk_send_push_messages
from shared.send_emails import custom_send_email
from shared.send_sms import broadcast_sms

@receiver(post_save, sender=Notice)
def my_handler(sender, instance, **kwargs):
    print("post save callback")
    print(instance.id)
    full_url = f"{settings.BASE_URL}/notices/{instance.id}"
    content = f"\n{strip_tags(instance.content)}\nView Notice - {full_url}"
    bulk_send_push_messages.delay({"title": "New Notice", "body": instance.title })
    custom_send_email.delay(instance.title, content)
    broadcast_sms.delay(instance.title, content)
