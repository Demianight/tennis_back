from django.contrib import admin

from .models import Match, Set, Game


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
