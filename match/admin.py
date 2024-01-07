from django.contrib import admin
from .models import Match, MatchCardRecord, MatchComment, MatchGoalRecord, MatchSubstituteRecord

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('teamA', 'teamB', 'status')
    list_filter = ('status',)
    search_fields = ('teamA__name', 'teamB__name')

@admin.register(MatchSubstituteRecord)
class MatchSubstituteRecordAdmin(admin.ModelAdmin):
    list_display = ('match',  'minute', 'created_at')
    list_filter = ('match', 'created_at')
    search_fields = ('match__teamA__name', 'match__teamB__name', 'player_in__name', 'player_out__name')

@admin.register(MatchCardRecord)
class MatchCardRecordAdmin(admin.ModelAdmin):
    list_display = ('match', 'card_type', 'penalty_time', 'minute', 'created_at')
    list_filter = ('match',  'card_type', 'created_at')
    search_fields = ('match__teamA__name', 'match__teamB__name', 'player__name')

@admin.register(MatchGoalRecord)
class MatchGoalRecordAdmin(admin.ModelAdmin):
    list_display = ('match',  'goal_minute', 'is_penalty_goal', 'is_own_goal', 'created_at')
    list_filter = ('match',  'goal_minute', 'is_penalty_goal', 'is_own_goal', 'created_at')
    search_fields = ('match__teamA__name', 'match__teamB__name', 'player__name')

@admin.register(MatchComment)
class MatchCommentAdmin(admin.ModelAdmin):
    list_display = ('match', 'comment_minute', 'comment', 'type', 'created_at')
    list_filter = ('match', 'comment_minute', 'type', 'created_at')
    search_fields = ('match__teamA__name', 'match__teamB__name', 'comment')