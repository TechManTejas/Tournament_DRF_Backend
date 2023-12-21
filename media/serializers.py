from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Media
        fields = '__all__'
