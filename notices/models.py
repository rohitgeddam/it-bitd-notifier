from django.db import models

# Create your models here.
class NoticeClass(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    files = models.FileField(upload_to="uploads/files", blank=True, null=True)

    def __str__(self):
        return self.title
