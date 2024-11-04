from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    last_activity = models.DateTimeField(blank=True, null=True, default=timezone.now)