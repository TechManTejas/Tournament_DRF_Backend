from rest_framework import viewsets

from tournament.models import Tournament
from .models import Round
from .serializers import RoundSerializer

class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

    def get_queryset(self):
        requester_club = self.request.user.club
        tournament_id = self.request.query_params.get("tournament_id")

        if tournament_id:
            # If tournament_id is provided, filter teams by both club and tournament
            return Round.objects.filter(club=requester_club, tournament__id=tournament_id)
        else:
            # If tournament_id is not provided, filter teams by club only
            return Round.objects.filter(club=requester_club)
        

    def perform_create(self, serializer):
        requester_club = self.request.user.club
        tournament_id = self.request.data.get("tournament_id", None)

        # Validate if the provided game_mode_id is valid
        try:
            tournament = Tournament.objects.get(pk=tournament_id)
        except Tournament.DoesNotExist:
            # Handle the case where the provided game_mode_id is not valid
            raise serializer.ValidationError("Invalid tournament_id")

        # Save the tournament with the associated club and game_mode
        serializer.save(club=requester_club, tournament=tournament)