from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import MatchViewSet

router = SimpleRouter()

router.register("matches", MatchViewSet, "matches")

urlpatterns = [
    path("", include(router.urls)),
]
