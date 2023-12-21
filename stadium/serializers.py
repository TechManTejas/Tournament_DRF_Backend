from rest_framework import serializers
from media.serializers import MediaSerializer
from .models import Stadium

class StadiumSerializer(serializers.ModelSerializer):
    image = MediaSerializer(read_only=True)
    class Meta:
        model = Stadium
        fields = '__all__'
