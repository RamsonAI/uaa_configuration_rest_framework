from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass
    # phone_number = models.CharField(max_length=10, unique=True)
