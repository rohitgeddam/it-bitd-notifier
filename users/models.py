from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# USER_TYPE_CHOICES = (
#       (1, 'student'),
#       (2, 'teacher'),
#       (3, 'secretary'),
#       (4, 'supervisor'),
#       (5, 'admin'),
#   )

class StudentProfile(models.Model):
    """StudentProfile Class"""
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    def __str__(self):
        return f"{self.user.username} profile"
    

class User(AbstractUser):
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    def __str__(self):
        return self.username
