from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)
    is_player = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ["id", "name", "email", "is_player", "password"]
