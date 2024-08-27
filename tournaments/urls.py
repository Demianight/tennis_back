from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import TournamentViewSet, TournamentParticipationViewSet

router = SimpleRouter()

router.register("tournaments", TournamentViewSet, "tournaments")
router.register(
    "participations", TournamentParticipationViewSet, "participations"
)

urlpatterns = [
    path("", include(router.urls)),
]
