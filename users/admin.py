from django.contrib import admin
from .models import User, Player


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
