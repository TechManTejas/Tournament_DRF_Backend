from rest_framework import serializers
from club.serializers import ClubSerializer
from round.serializers import RoundSerializer
from team.serializers import TeamRecordSerializer
from tournament.serializers import TournamentSerializer
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    round = RoundSerializer(read_only=True)
    tournament = TournamentSerializer(read_only=True)
    team_records = TeamRecordSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'
