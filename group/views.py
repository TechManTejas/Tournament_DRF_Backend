import json
from rest_framework import viewsets
from round.models import Round

from tournament.models import Tournament
from .models import Group
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        requester_club = self.request.user.club
        tournament_id = self.request.query_params.get("tournament_id")
        round_id = self.request.query_params.get("round_id")

        queryset = Group.objects.filter(club=requester_club)

        if tournament_id:
            queryset = queryset.filter(tournament__id=tournament_id)

        if round_id:
            queryset = queryset.filter(round__id=round_id)

        return queryset
        
    def perform_create(self, serializer):
        requester_club = self.request.user.club
        tournament_id = self.request.data.get('tournament_id')
        round_id = self.request.data.get('round_id')

        tournament = Tournament.objects.get(id=tournament_id)
        round_instance = Round.objects.get(id=round_id)

        # Save the group instance without the team_records field first
        group_instance = serializer.save(
            club=requester_club, 
            tournament=tournament, 
            round=round_instance,
        )

        # Handle the many-to-many relationship for team_records
        team_records_data = self.request.data.get('team_records', [])
        for team_record_id in json.loads(team_records_data):
            # Assuming team_records is a ManyToManyField in the Group model
            group_instance.team_records.add(team_record_id)

        # Finally, save the group_instance with the updated team_records
        group_instance.save()

    def perform_update(self, serializer):
        # Retrieve the existing group instance
        instance = self.get_object()

        # Clear existing team_records
        instance.team_records.clear()

        # Handle the many-to-many relationship for team_records
        team_records_data = self.request.data.get('team_records', [])
        team_records_ids = json.loads(team_records_data)

        # Assuming the order is sent as a list of dictionaries with 'id' and 'order' keys
        for order, data in enumerate(team_records_ids):
            team_record_id = data['id']

            # Add team_record to the group with the specified order
            instance.team_records.add(team_record_id, through_defaults={'order': order})

        # Update the other fields using the serializer
        serializer.save()