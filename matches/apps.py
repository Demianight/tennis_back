from django.apps import AppConfig


class MatchesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "matches"

    def ready(self) -> None:
        import matches.signals  # noqa

        return super().ready()
