from django.db import models
from ckeditor.fields import RichTextField

from core.models import YearTag


OFFER_TYPE = (("I", "Internship"), ("J", "Job"))
APPLICATION_TYPE = (("OF", "Off Campus"), ("ON", "On Campus"))


class Job(models.Model):
    """Job class"""

    title = models.CharField(max_length=64)
    job_description = RichTextField()
    application_link = models.URLField(null=True, blank=True)
    year_tags = models.ManyToManyField(YearTag, related_name="job")
    offer_type = models.CharField(max_length=1, choices=OFFER_TYPE)
    application_type = models.CharField(max_length=2, choices=APPLICATION_TYPE)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .tasks import broadcast_sms, custom_send_email

# from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=Job)
def my_handler(sender, instance, **kwargs):
    print("post save callback")
    print(instance.id)
    full_url = f"{settings.BASE_URL}/jobs/{instance.id}"

    content = f"\n{strip_tags(instance.job_description)}\nView Job Post - {full_url}"
    custom_send_email.delay(instance.title, content)
    broadcast_sms.delay(instance.title, content)
