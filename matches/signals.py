from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Match


@receiver(post_save, sender=Match)
def create_next_match(sender, instance: Match, **kwargs):
    actual_round = instance.round_number + (
        1 if instance.round_number % 2 else -1
    )
    previous_match2 = Match.objects.filter(
        tournament=instance.tournament,
        round_number=actual_round,
    ).first()
    if previous_match2 and instance.winner and previous_match2.winner:
        Match.objects.get_or_create(
            tournament=instance.tournament,
            player1=instance.winner,
            player2=previous_match2.winner,
            round_number=(actual_round - 1) // 2,
        )
