from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'squad_number')
    list_filter = ('club',)
    search_fields = ('name', 'club__name', 'squad_number')
