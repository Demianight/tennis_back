from django.db import models

from users.models import Player
from tournaments.models import Tournament

score_choices = [(0, 0), (15, 15), (30, 30), (40, 40)]


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

    first_play = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="first_plays",
    )

    def __str__(self):
        return f"{self.player1.user.username} vs {self.player2.user.username} in {self.tournament.name}, round: {self.round_number}"


class Set(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="sets",
        verbose_name="Матч",
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Победитель",
    )
    number = models.PositiveIntegerField(verbose_name="Номер сета")

    class Meta:
        verbose_name = "Сет"
        verbose_name_plural = "Сеты"


class Game(models.Model):
    set = models.ForeignKey(
        Set,
        on_delete=models.CASCADE,
        related_name="games",
        verbose_name="Сет",
    )
    number = models.PositiveIntegerField(verbose_name="Номер гейма")

    score1 = models.PositiveIntegerField(choices=score_choices, default=0)
    score2 = models.PositiveIntegerField(choices=score_choices, default=0)

    tiebreak = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Гейм"
        verbose_name_plural = "Геймы"
