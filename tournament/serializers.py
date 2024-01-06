from rest_framework import serializers
from club.serializers import ClubSerializer
from .models import Tournament
from .models import GameMode


class GameModeSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = GameMode
        fields = "__all__"


class TournamentSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    game_mode = GameModeSerializer(read_only=True)

    class Meta:
        model = Tournament
        fields = "__all__"
