from django.db import models

from core.models import YearTag


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
