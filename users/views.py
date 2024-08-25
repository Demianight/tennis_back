from rest_framework.viewsets import ModelViewSet
from .permissions import IsSelfOrReadOnly
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly]

    def get_queryset(self):
        return User.objects.all()
