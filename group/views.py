import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from round.models import Round
from team.models import TeamRecord
from django.db import transaction
from tournament.models import Tournament
from .models import Group, GroupTeam
from .serializers import GroupSerializer, GroupTeamSerializer


class GroupTeamViewSet(viewsets.ModelViewSet):
    queryset = GroupTeam.objects.all()
    serializer_class = GroupTeamSerializer


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

    def create(self, request, *args, **kwargs):
        requester_club = request.user.club
        tournament_id = request.data.get("tournament_id")
        round_id = request.data.get("round_id")

        tournament = Tournament.objects.get(id=tournament_id)
        round_instance = Round.objects.get(id=round_id)
        group_team_records = []

        # Handle the many-to-many relationship for team_records
        group_team_records_data = request.data.get("group_team_records", [])
        group_team_record_orders_ids = json.loads(group_team_records_data)

        for team_obj in group_team_record_orders_ids:
            team_record_instance = TeamRecord.objects.get(id=team_obj["id"])

            # Create GroupTeam instance with the order attribute
            group_team_instance = GroupTeam.objects.create(
                team_record=team_record_instance,
                order=team_obj["order"],
            )
            group_team_records.append(group_team_instance.id)

        # Create Group object at the last
        with transaction.atomic():
            group_instance = Group.objects.create(
                club=requester_club,
                tournament=tournament,
                round=round_instance,
                name=request.data.get(
                    "name"
                ),  # Add the field name as per your serializer
            )

            # Set the many-to-many relationship for team_records
            group_instance.group_team_records.set(group_team_records)

        return Response(
            {"status": "Group created successfully"}, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance:
            serializer = self.get_serializer(
                instance, data=request.data
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            # Update the related group team records if needed
            group_team_records_data = request.data.get("group_team_records", [])
            group_team_records_data = json.loads(group_team_records_data)

            for team_obj in group_team_records_data:
                team_record_id = team_obj["id"]
                group_team_id = team_obj["group_team_id"]
                order = team_obj["order"]
                

                try:
                    team_record = TeamRecord.objects.get(id=team_record_id)
                    group_team_instance = GroupTeam.objects.get(id=group_team_id)
                    
                    group_team_instance.order = order
                    group_team_instance.team_record = team_record
                    group_team_instance.save()

                except GroupTeam.DoesNotExist:
                    return Response(
                        {
                            "error": f"GroupTeam with ID {team_record_id} does not exist."
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )
                except TeamRecord.DoesNotExist:
                    return Response(
                        {
                            "error": f"TeamRecord with ID {team_record_id} does not exist."
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )

            return Response(serializer.data)
        else:
            return Response(
                {"error": "Group not found"}, status=status.HTTP_404_NOT_FOUND
            )
