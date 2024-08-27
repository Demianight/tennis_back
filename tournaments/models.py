from django.db import models
from users.models import Player


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100, null=True, blank=True)
    players = models.ManyToManyField(
        Player, through="TournamentParticipation", related_name="tournaments"
    )
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TournamentParticipation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    seed = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.player.user.first_name} {self.player.user.last_name} in {self.tournament.name}"
