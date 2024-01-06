from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from group.models import Group

from round.models import Round
from .models import GameMode, Tournament
from .serializers import GameModeSerializer, TournamentSerializer


class GameModeViewSet(viewsets.ModelViewSet):
    queryset = GameMode.objects.all()
    serializer_class = GameModeSerializer


class TournamentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    filter_backends = [SearchFilter]
    search_fields = ["^name", "^alias"]
    pagination_class = TournamentPagination

    def get_queryset(self):
        requester_club = self.request.user.club
        return Tournament.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        requester_club = self.request.user.club
        game_mode_id = self.request.data.get("game_mode", None)

        # Validate if the provided game_mode_id is valid
        try:
            game_mode = GameMode.objects.get(pk=game_mode_id)
        except GameMode.DoesNotExist:
            # Handle the case where the provided game_mode_id is not valid
            raise serializer.ValidationError("Invalid game_mode_id")

        # Save the tournament with the associated club and game_mode
        serializer.save(club=requester_club, game_mode=game_mode)

        # Create rounds, groups, and schedules based on the game mode data
        self.create_rounds_groups_schedules(serializer.instance, game_mode.data)

    def create_rounds_groups_schedules(self, tournament, game_mode_data):
        for round_data in game_mode_data:
            groups_data = round_data.get("groups", [])

            # Explicitly pass tournament_id and club_id when creating Round
            round_obj = Round.objects.create(
                tournament=tournament,
                club=tournament.club,
                name=round_data["name"],
                no_of_groups=len(groups_data)
            )

            # Create Groups
            for group_data in groups_data:
                group_obj = Group.objects.create(
                    tournament=tournament,
                    round=round_obj,
                    club=tournament.club,
                    name=group_data["name"]
                )