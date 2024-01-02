from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from player.models import Player

from tournament.models import Tournament
from .models import TeamRecord
from .serializers import TeamRecordSerializer


class TeamPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class TeamRecordViewSet(viewsets.ModelViewSet):
    queryset = TeamRecord.objects.all()
    serializer_class = TeamRecordSerializer
    pagination_class = TeamPagination
    filter_backends = [SearchFilter]
    search_fields = ["^name"]

    def get_queryset(self):
        requester_club = self.request.user.club
        tournament_id = self.request.query_params.get("tournament_id")

        if tournament_id:
            # If tournament_id is provided, filter teams by both club and tournament
            return TeamRecord.objects.filter(club=requester_club, tournament__id=tournament_id)
        else:
            # If tournament_id is not provided, filter teams by club only
            return TeamRecord.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        # Get or create the tournament instance
        tournament_id = self.request.data.get("tournament")

        tournament_instance = Tournament.objects.get(id=int(tournament_id))

        playing_players_ids = [
            self.request.data.get(f"playing_player_{i}") 
            for i in range(1, 12)
            if self.request.data.get(f"playing_player_{i}") is not None and self.request.data.get(f"playing_player_{i}") != 'undefined'
        ]

        playing_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in playing_players_ids
        ]

        substitute_players_ids = [
            self.request.data.get(f"substitute_player_{i}") 
            for i in range(1, 6)
            if self.request.data.get(f"substitute_player_{i}") is not None and self.request.data.get(f"substitute_player_{i}") != 'undefined'
        ]
        substitute_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in substitute_players_ids
        ]

        # Set the club for the team record
        serializer.save(
            club=self.request.user.club,
            tournament=tournament_instance,
            playing_player_1=playing_players_instances[0],
            playing_player_2=playing_players_instances[1] if len(playing_players_instances) > 1 else None,
            playing_player_3=playing_players_instances[2] if len(playing_players_instances) > 2 else None,
            playing_player_4=playing_players_instances[3] if len(playing_players_instances) > 3 else None,
            playing_player_5=playing_players_instances[4] if len(playing_players_instances) > 4 else None,
            playing_player_6=playing_players_instances[5] if len(playing_players_instances) > 5 else None,
            playing_player_7=playing_players_instances[6] if len(playing_players_instances) > 6 else None,
            playing_player_8=playing_players_instances[7] if len(playing_players_instances) > 7 else None,
            playing_player_9=playing_players_instances[8] if len(playing_players_instances) > 8 else None,
            playing_player_10=playing_players_instances[9] if len(playing_players_instances) > 9 else None,
            playing_player_11=playing_players_instances[10] if len(playing_players_instances) > 10 else None,
            substitute_player_1=substitute_players_instances[0] if len(substitute_players_instances) > 0 else None,
            substitute_player_2=substitute_players_instances[1] if len(substitute_players_instances) > 1 else None,
            substitute_player_3=substitute_players_instances[2] if len(substitute_players_instances) > 2 else None,
            substitute_player_4=substitute_players_instances[3] if len(substitute_players_instances) > 3 else None,
            substitute_player_5=substitute_players_instances[4] if len(substitute_players_instances) > 4 else None,
        )

    def perform_update(self, serializer):
        # Update the tournament instance if the tournament_id is provided
        tournament_id = self.request.data.get("tournament")
        if tournament_id:
            tournament_instance = Tournament.objects.get(id=int(tournament_id))
            serializer.save(tournament=tournament_instance)
        else:
            serializer.save()

        # Update playing players if provided in the request data
        playing_players_ids = [
            self.request.data.get(f"playing_player_{i}") 
            for i in range(1, 12)
            if self.request.data.get(f"playing_player_{i}") is not None and self.request.data.get(f"playing_player_{i}") != 'undefined'
        ]
        playing_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in playing_players_ids
        ]

        # Update substitute players if provided in the request data
        substitute_players_ids = [
            self.request.data.get(f"substitute_player_{i}") 
            for i in range(1, 6)
            if self.request.data.get(f"substitute_player_{i}") is not None and self.request.data.get(f"substitute_player_{i}") != 'undefined'
        ]
        substitute_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in substitute_players_ids
        ]

        # Update playing players and substitute players in the team record
        serializer.save(
            club=self.request.user.club,
            tournament=tournament_instance,
            playing_player_1=playing_players_instances[0],
            playing_player_2=playing_players_instances[1] if len(playing_players_instances) > 1 else None,
            playing_player_3=playing_players_instances[2] if len(playing_players_instances) > 2 else None,
            playing_player_4=playing_players_instances[3] if len(playing_players_instances) > 3 else None,
            playing_player_5=playing_players_instances[4] if len(playing_players_instances) > 4 else None,
            playing_player_6=playing_players_instances[5] if len(playing_players_instances) > 5 else None,
            playing_player_7=playing_players_instances[6] if len(playing_players_instances) > 6 else None,
            playing_player_8=playing_players_instances[7] if len(playing_players_instances) > 7 else None,
            playing_player_9=playing_players_instances[8] if len(playing_players_instances) > 8 else None,
            playing_player_10=playing_players_instances[9] if len(playing_players_instances) > 9 else None,
            playing_player_11=playing_players_instances[10] if len(playing_players_instances) > 10 else None,
            substitute_player_1=substitute_players_instances[0] if len(substitute_players_instances) > 0 else None,
            substitute_player_2=substitute_players_instances[1] if len(substitute_players_instances) > 1 else None,
            substitute_player_3=substitute_players_instances[2] if len(substitute_players_instances) > 2 else None,
            substitute_player_4=substitute_players_instances[3] if len(substitute_players_instances) > 3 else None,
            substitute_player_5=substitute_players_instances[4] if len(substitute_players_instances) > 4 else None,
        )