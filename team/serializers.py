from rest_framework import serializers
from club.serializers import ClubSerializer
from player.serializers import PlayerSerializer
from .models import TeamRecord

class TeamRecordSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    playing_player_1 = PlayerSerializer(read_only=True)
    playing_player_2 = PlayerSerializer(read_only=True)
    playing_player_3 = PlayerSerializer(read_only=True)
    playing_player_4 = PlayerSerializer(read_only=True)
    playing_player_5 = PlayerSerializer(read_only=True)
    playing_player_6 = PlayerSerializer(read_only=True)
    playing_player_7 = PlayerSerializer(read_only=True)
    playing_player_8 = PlayerSerializer(read_only=True)
    playing_player_9 = PlayerSerializer(read_only=True)
    playing_player_10 = PlayerSerializer(read_only=True)
    playing_player_11 = PlayerSerializer(read_only=True)
    substitute_player_1 = PlayerSerializer(read_only=True)
    substitute_player_2 = PlayerSerializer(read_only=True)
    substitute_player_3 = PlayerSerializer(read_only=True)
    substitute_player_4 = PlayerSerializer(read_only=True)
    substitute_player_5 = PlayerSerializer(read_only=True)

    class Meta:
        model = TeamRecord
        fields = '__all__'
