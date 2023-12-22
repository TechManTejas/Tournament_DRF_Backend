from rest_framework import serializers

from club.serializers import ClubSerializer
from .models import Referee

class RefereeSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True) 
    class Meta:
        model = Referee
        fields = '__all__'
