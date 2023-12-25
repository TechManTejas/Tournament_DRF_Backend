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
        print(self.request.data)

        # Get or create the tournament instance
        tournament_id = self.request.data.get("tournament")

        tournament_instance = Tournament.objects.get(id=int(tournament_id))

        playing_players_ids = [
            self.request.data.get(f"playing_player_{i}") for i in range(1, 12)
        ]
        playing_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in playing_players_ids
        ]

        substitute_players_ids = [
            self.request.data.get(f"substitute_player_{i}") for i in range(1, 6)
        ]
        substitute_players_instances = [
            Player.objects.get(id=int(player_id)) for player_id in substitute_players_ids
        ]

        # Set the club for the team record
        serializer.save(
            club=self.request.user.club,
            tournament=tournament_instance,
            playing_player_1=playing_players_instances[0],
            playing_player_2=playing_players_instances[1],
            playing_player_3=playing_players_instances[2],
            playing_player_4=playing_players_instances[3],
            playing_player_5=playing_players_instances[4],
            playing_player_6=playing_players_instances[5],
            playing_player_7=playing_players_instances[6],
            playing_player_8=playing_players_instances[7],
            playing_player_9=playing_players_instances[8],
            playing_player_10=playing_players_instances[9],
            playing_player_11=playing_players_instances[10],
            substitute_player_1=substitute_players_instances[0],
            substitute_player_2=substitute_players_instances[1],
            substitute_player_3=substitute_players_instances[2],
            substitute_player_4=substitute_players_instances[3],
            substitute_player_5=substitute_players_instances[4],
        )
