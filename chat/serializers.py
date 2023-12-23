from rest_framework import serializers
from user.serializers import UserSerializer
from club.serializers import ClubSerializer
from .models import ChatSupport, ChatClub

class ChatSupportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    club = ClubSerializer(read_only=True)

    class Meta:
        model = ChatSupport
        fields = '__all__'

class ChatClubSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    club = ClubSerializer(read_only=True)

    class Meta:
        model = ChatClub
        fields = '__all__'
