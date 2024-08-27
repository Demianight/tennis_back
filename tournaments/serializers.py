from rest_framework import serializers
from users.serializers import PlayerSerializer
from matches.serializers import MatchSerializer

from .models import Tournament, TournamentParticipation


class TournamentParticipationSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = TournamentParticipation
        fields = ["id", "player", "tournament", "seed"]


class TournamentSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    matches = MatchSerializer(many=True)

    class Meta:
        model = Tournament
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "location",
            "is_active",
            "players",
            "matches",
        ]
