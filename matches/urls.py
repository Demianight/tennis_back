from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import MatchViewSet, GameViewSet, SetViewSet

router = SimpleRouter()

router.register("matches", MatchViewSet, "matches")
router.register("games", GameViewSet, "games")
router.register("sets", SetViewSet, "sets")

urlpatterns = [
    path("", include(router.urls)),
]
