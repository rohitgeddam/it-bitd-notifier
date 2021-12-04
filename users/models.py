from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator


# USER_TYPE_CHOICES = (
#       (1, 'student'),
#       (2, 'teacher'),
#       (3, 'secretary'),
#       (4, 'supervisor'),
#       (5, 'admin'),
#   )

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


# class StudentProfile(models.Model):
#     """StudentProfile Class"""

#     user = models.OneToOneField("User", on_delete=models.CASCADE)

#     # email = models.EmailField(null=True, blank=True)

#     # is_email_verified = models.BooleanField(default=False)
#     # is_mobile_verified = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.user.username} profile"


class User(AbstractUser):
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    email = models.EmailField("email address", blank=False, unique=True)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True, unique=True
    )  # validators should be a list
    batch = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
        null=True,
        blank=True,
    )
    receive_email_notification = models.BooleanField(default=True)
    receive_sms_notification = models.BooleanField(default=True)
    objects = UserManager()

    def save(self, *args, **kwargs):
        """override save method"""
        super().save(*args, **kwargs)
        try:
            new_profile = StudentProfile.objects.create(user=self)
            print(new_profile)
        except:
            print("falied")

    def __str__(self):
        return self.username
