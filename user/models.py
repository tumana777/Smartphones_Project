from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    last_activity = models.DateTimeField(blank=True, null=True)