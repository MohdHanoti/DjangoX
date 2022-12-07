from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Country=models.CharField(max_length=50,default='Jordan')

    def __str__(self):
        return self.email