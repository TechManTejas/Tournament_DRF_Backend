from rest_framework import serializers
from club.serializers import ClubSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email', 'password', 'role', 'message', 'verified', 'club']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}