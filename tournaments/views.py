from rest_framework import viewsets

from .models import Tournament, TournamentParticipation
from .serializers import (
    TournamentParticipationSerializer,
    TournamentSerializer,
)


class TournamentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tournament.objects.all().prefetch_related(
        "matches",
        "matches__player1",
        "matches__player2",
    )
    serializer_class = TournamentSerializer


class TournamentParticipationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TournamentParticipation.objects.all()
    serializer_class = TournamentParticipationSerializer
