from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_player = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.email}"
