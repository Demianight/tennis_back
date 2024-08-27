from django.contrib.auth.models import AbstractUser

from django.db import models
from rest_framework.exceptions import ValidationError


class User(AbstractUser):
    is_player = models.BooleanField(default=False)


class Player(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="player_profile"
    )
    rank = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if Player.objects.filter(user=self.user).exists():
            raise ValidationError(
                f"A player profile for the user {self.user.username} already exists."
            )
        super().save(*args, **kwargs)
