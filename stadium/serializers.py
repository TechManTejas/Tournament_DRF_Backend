from rest_framework import serializers
from club.serializers import ClubSerializer
from .models import Stadium

class StadiumSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    class Meta:
        model = Stadium
        fields = "__all__"