from rest_framework import serializers

from .models import Match
from users.serializers import PlayerSerializer


class MatchSerializer(serializers.ModelSerializer):
    tournament = serializers.StringRelatedField()
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    winner = PlayerSerializer(allow_null=True)

    score = serializers.SerializerMethodField()

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
            "score1",
            "score2",
            "score",
        ]

    def get_score(self, obj: Match) -> str:
        return f"{obj.score1}-{obj.score2}"
