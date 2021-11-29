from django.db import models


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
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.date}"
