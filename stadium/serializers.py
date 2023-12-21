from rest_framework import serializers
from media.serializers import MediaSerializer
from .models import Stadium

class StadiumReadSerializer(serializers.ModelSerializer):
    image = MediaSerializer(read_only=True)
    class Meta:
        model = Stadium
        fields = "__all__"


# Serializer for write operation (create or update)
class StadiumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"
