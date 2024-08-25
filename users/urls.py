from rest_framework.routers import SimpleRouter
from .views import UserViewSet
from django.urls import path, include

router = SimpleRouter()
router.register("users", UserViewSet, "users")

urlpatterns = [
    path("", include(router.urls)),
]
