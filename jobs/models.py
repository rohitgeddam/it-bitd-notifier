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
