from rest_framework import serializers

from .models import Match, Set, Game
from tournaments.models import Tournament
from users.serializers import PlayerSerializer


class MatchSerializer(serializers.ModelSerializer):
    tournament = serializers.PrimaryKeyRelatedField(
        queryset=Tournament.objects.all()
    )
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    winner = PlayerSerializer(allow_null=True)

    class Meta:
        model = Match
        fields = [
            "id",
            "tournament",
            "player1",
            "player2",
            "winner",
            "match_date",
            "round_number",
        ]


class SetSerializer(serializers.ModelSerializer):
    match = serializers.PrimaryKeyRelatedField(queryset=Match.objects.all())

    class Meta:
        model = Set
        fields = ["id", "match", "winner", "number"]


class GameSerializer(serializers.ModelSerializer):
    set = serializers.PrimaryKeyRelatedField(queryset=Set.objects.all())

    class Meta:
        model = Game
        fields = ["id", "set", "number", "score1", "score2"]
