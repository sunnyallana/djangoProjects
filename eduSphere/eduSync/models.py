from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    user = (
        (1, "departmentHead"),
        (2, "faculty"),
        (3, "student"),
    )
    userType = models.CharField(choices = user, max_length = 50, default = 1)
    profilePicture = models.ImageField(upload_to = 'media/profilePicture')

