from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'club', 'squad_number')
    list_filter = ('team', 'club')
    search_fields = ('name', 'team__name', 'club__name', 'squad_number')
