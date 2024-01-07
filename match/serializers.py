from rest_framework import serializers
from club.serializers import ClubSerializer
from group.serializers import GroupSerializer, GroupTeamSerializer
from player.serializers import PlayerSerializer
from referee.serializers import RefereeSerializer
from round.serializers import RoundSerializer
from stadium.serializers import StadiumSerializer
from team.serializers import TeamRecordSerializer
from tournament.serializers import TournamentSerializer
from .models import (
    Match,
    MatchCardRecord,
    MatchComment,
    MatchGoalRecord,
    MatchSubstituteRecord,
)


class MatchSerializer(serializers.ModelSerializer):
    teamA = GroupTeamSerializer(read_only=True)
    teamB = GroupTeamSerializer(read_only=True)
    referee_head = RefereeSerializer(read_only=True)
    referee_assistant = RefereeSerializer(read_only=True)
    referee_assistant_2 = RefereeSerializer(read_only=True)
    referee_assistant_3 = RefereeSerializer(read_only=True)
    stadium = StadiumSerializer(read_only=True)

    class Meta:
        model = Match
        fields = "__all__"


class MatchSubstituteRecordSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    match = MatchSerializer(read_only=True)
    player_in = PlayerSerializer(read_only=True)
    player_out = PlayerSerializer(read_only=True)
    class Meta:
        model = MatchSubstituteRecord
        fields = "__all__"


class MatchCardRecordSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    match = MatchSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)
    class Meta:
        model = MatchCardRecord
        fields = "__all__"


class MatchGoalRecordSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    match = MatchSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)
    class Meta:
        model = MatchGoalRecord
        fields = "__all__"


class MatchCommentSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    match = MatchSerializer(read_only=True)
    class Meta:
        model = MatchComment
        fields = "__all__"
