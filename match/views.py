from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import F

from group.models import GroupTeam
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

    def create(self, request, *args, **kwargs):

        print(request.data)

        try:
            # Extract data from the request
            match_id = request.data.get('match')
            group_team_record_id = request.data.get('group_team_record')
            player_id = request.data.get('player')
            card_type = request.data.get('card_type')
            penalty_time = request.data.get('penalty_time', None)
            minute = request.data.get('minute')

            # Create the MatchCardRecord object
            card_record = MatchCardRecord.objects.create(
                match_id=match_id,
                group_team_record_id=group_team_record_id,
                player_id=player_id,
                card_type=card_type,
                penalty_time=penalty_time,
                minute=minute
            )

            # Serialize the created object
            serializer = self.get_serializer(card_record)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




class MatchGoalRecordViewSet(viewsets.ModelViewSet):
    queryset = MatchGoalRecord.objects.all()
    serializer_class = MatchGoalRecordSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Extract data from the request
            match_id = request.data.get('match')
            group_team_record_id = request.data.get('group_team_record') 
            other_group_team_record_id = request.data.get('other_group_team_record')
            player_id = request.data.get('player')
            is_standard_goal = request.data.get('is_standard_goal', False)
            is_penalty_goal = request.data.get('is_penalty_goal', False)
            is_own_goal = request.data.get('is_own_goal', False)

            # Create the MatchGoalRecord object
            goal_record = MatchGoalRecord.objects.create(
                match_id=match_id,
                group_team_record_id=group_team_record_id,
                player_id=player_id,
                is_standard_goal=is_standard_goal,
                is_penalty_goal=is_penalty_goal,
                is_own_goal=is_own_goal
            )

            # Get the corresponding GroupTeam object
            group_team = GroupTeam.objects.get(id=group_team_record_id)
            other_group_team = GroupTeam.objects.get(id=other_group_team_record_id)

            # Increment goals_pos if the goal was standard or penalty
            if is_standard_goal or is_penalty_goal:
                GroupTeam.objects.filter(id=group_team.id).update(goals_pos=F('goals_pos') + 1)
                GroupTeam.objects.filter(id=other_group_team.id).update(goals_neg=F('goals_neg') + 1)

            # If it's an own goal, increment goals_pos of the other_group_team
            elif is_own_goal:
                GroupTeam.objects.filter(id=other_group_team.id).update(goals_pos=F('goals_pos') + 1)
                GroupTeam.objects.filter(id=group_team.id).update(goals_neg=F('goals_neg') + 1)

            # Serialize the created object
            serializer = self.get_serializer(goal_record)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MatchCommentViewSet(viewsets.ModelViewSet):
    queryset = MatchComment.objects.all()
    serializer_class = MatchCommentSerializer
