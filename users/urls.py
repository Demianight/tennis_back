from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PlayerViewSet
from django.urls import path, include

router = SimpleRouter()
router.register("users", UserViewSet, "users")
router.register("players", PlayerViewSet, "players")

urlpatterns = [
    path("", include(router.urls)),
]
