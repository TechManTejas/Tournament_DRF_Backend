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

    def update(self, request, *args, **kwargs):
        # Extract match_id from request.data
        match_id = request.data.get('id')
        
        # Retrieve the instance to be updated using match_id
        try:
            instance = Match.objects.get(pk=match_id)
        except Match.DoesNotExist:
            return Response({'detail': 'Match not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the instance with the rest of the information from request.data
        instance.status = request.data.get('status', instance.status)
        instance.stadium_id = request.data.get('stadium', instance.stadium_id)
        instance.referee_head_id = request.data.get('refereeHead', instance.referee_head_id)
        instance.referee_assistant_id = request.data.get('refereeAssistant1', instance.referee_assistant_id)
        instance.referee_assistant_2_id = request.data.get('refereeAssistant2', instance.referee_assistant_2_id)
        instance.referee_assistant_3_id = request.data.get('refereeAssistant3', instance.referee_assistant_3_id)
        instance.jersey_color_A = request.data.get('jersey_color_A', instance.jersey_color_A)
        instance.jersey_color_B = request.data.get('jersey_color_B', instance.jersey_color_B)

        # Save the updated instance
        instance.save()

        return Response({'detail': 'Match updated successfully'}, status=status.HTTP_200_OK)
    
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
