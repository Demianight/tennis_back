from django.contrib import admin

from .models import Tournament, TournamentParticipation


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    pass


@admin.register(TournamentParticipation)
class TournamentParticipationAdmin(admin.ModelAdmin):
    pass
