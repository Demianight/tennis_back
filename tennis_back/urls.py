from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", include("users.urls")),
    path("", include("tokens.urls")),
    path("", include("tournaments.urls")),
    path("", include("matches.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]
