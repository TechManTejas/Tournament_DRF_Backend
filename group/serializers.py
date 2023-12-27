from rest_framework import serializers
from club.serializers import ClubSerializer
from round.serializers import RoundSerializer
from team.serializers import TeamRecordSerializer
from tournament.serializers import TournamentSerializer
from .models import Group, GroupTeam

class GroupTeamSerializer(serializers.ModelSerializer):
    team_record = TeamRecordSerializer(read_only=True)
    class Meta:
        model = GroupTeam
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    round = RoundSerializer(read_only=True)
    tournament = TournamentSerializer(read_only=True)
    group_team_records = GroupTeamSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'
