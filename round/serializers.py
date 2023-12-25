from rest_framework import serializers
from club.serializers import ClubSerializer
from tournament.serializers import TournamentSerializer
from .models import Round

class RoundSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    tournament = TournamentSerializer(read_only=True)
    class Meta:
        model = Round
        fields = '__all__'
