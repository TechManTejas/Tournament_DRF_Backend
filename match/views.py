from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    Match,
    MatchCardRecord,
    MatchComment,
    MatchGoalRecord,
    MatchSubstituteRecord,
)
from .serializers import (
    MatchCardRecordSerializer,
    MatchCommentSerializer,
    MatchGoalRecordSerializer,
    MatchSerializer,
    MatchSubstituteRecordSerializer,
)


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def create(self, request, *args, **kwargs):
        # Use the serializer to handle data validation and extraction
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract relevant data from the serializer
        teamA_id = request.data.get('teamA')
        teamB_id = request.data.get('teamB')

        # Generate the match ID using the concatenated team IDs
        match_id = f"{teamA_id}-{teamB_id}"

        # Check if the match with the generated ID already exists
        match = Match.objects.filter(pk=match_id).first()

        if match:
            return Response({"detail": "Match with the same teams already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Continue with the normal creation process using Match.objects.create
        Match.objects.create(
            teamA_id=teamA_id,
            teamB_id=teamB_id,
            id=match_id
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
