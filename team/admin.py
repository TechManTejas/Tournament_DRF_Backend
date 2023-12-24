from django.contrib import admin
from .models import TeamRecord

@admin.register(TeamRecord)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'short_name', 'verified', 'save_team')
    list_filter = ('club', 'verified', 'save_team')
    search_fields = ('name', 'short_name')

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'club', 'logo', 'short_name', 'verified')
        }),
        ('Playing Players', {
            'fields': (
                'playing_player_1', 'playing_player_2', 'playing_player_3', 'playing_player_4',
                'playing_player_5', 'playing_player_6', 'playing_player_7', 'playing_player_8',
                'playing_player_9', 'playing_player_10', 'playing_player_11'
            )
        }),
        ('Substitute Players', {
            'fields': (
                'substitute_player_1', 'substitute_player_2', 'substitute_player_3',
                'substitute_player_4', 'substitute_player_5'
            )
        }),
        ('Additional Attributes', {
            'fields': ('save_team',)
        }),
    )

    def save_team_display(self, obj):
        return obj.save_team
    save_team_display.short_description = 'Save Team'
    save_team_display.boolean = True
