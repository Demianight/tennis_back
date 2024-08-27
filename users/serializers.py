from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Player


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_player",
        ]


class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ["id", "user", "rank", "bio", "birth_date"]
