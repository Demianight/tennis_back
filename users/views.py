from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tokens.permissions import IsOwnerOrReadOnly
from .permissions import IsSelfOrReadOnly
from .serializers import UserSerializer, PlayerSerializer
from .models import Player, User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly]

    def get_queryset(self):
        return User.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Player.objects.all()

    def perform_create(self, serializer: PlayerSerializer):
        return serializer.save(user=self.request.user)
