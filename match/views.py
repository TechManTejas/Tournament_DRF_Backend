from rest_framework import viewsets
from .models import Match, MatchCardRecord, MatchComment, MatchGoalRecord, MatchSubstituteRecord
from .serializers import MatchCardRecordSerializer, MatchCommentSerializer, MatchGoalRecordSerializer, MatchSerializer, MatchSubstituteRecordSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchSubstituteRecordViewSet(viewsets.ModelViewSet):
    queryset = MatchSubstituteRecord.objects.all()
    serializer_class = MatchSubstituteRecordSerializer

class MatchCardRecordViewSet(viewsets.ModelViewSet):
    queryset = MatchCardRecord.objects.all()
    serializer_class = MatchCardRecordSerializer

class MatchGoalRecordViewSet(viewsets.ModelViewSet):
    queryset = MatchGoalRecord.objects.all()
    serializer_class = MatchGoalRecordSerializer

class MatchCommentViewSet(viewsets.ModelViewSet):
    queryset = MatchComment.objects.all()
    serializer_class = MatchCommentSerializer