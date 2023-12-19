from rest_framework import serializers
from .models import Match, MatchCardRecord, MatchComment, MatchGoalRecord, MatchSubstituteRecord

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MatchSubstituteRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchSubstituteRecord
        fields = '__all__'

class MatchCardRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchCardRecord
        fields = '__all__'

class MatchGoalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchGoalRecord
        fields = '__all__'

class MatchCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchComment
        fields = '__all__'