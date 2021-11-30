from django.db import models

# Create your models here.
class YearTag(models.Model):
    """Class For Tags"""

    title = models.CharField(max_length=16)
    year = models.IntegerField()

    def __str__(self):
        return self.title
