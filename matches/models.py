from django.db import models

from users.models import Player
from tournaments.models import Tournament


class Match(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="matches"
    )
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player1_matches"
    )
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player2_matches"
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wins",
    )
    match_date = models.DateTimeField(null=True, blank=True)
    round_number = models.PositiveIntegerField()

    score1 = models.PositiveIntegerField(default=0)
    score2 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player1.user.username} vs {self.player2.user.username} in {self.tournament.name}, score: {self.score1}-{self.score2}, round: {self.round_number}"
