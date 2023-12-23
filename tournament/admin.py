from django.contrib import admin
from .models import Tournament
from .models import GameMode

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'start_date', 'start_time')

@admin.register(GameMode)
class GameModeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)