import random
import string
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=16, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'phone']

    def __str__(self):
        return self.name

