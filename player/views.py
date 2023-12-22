from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Player
from .serializers import PlayerSerializer  

class PlayerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter]
    search_fields = ["^name"]
    pagination_class = PlayerPagination

    def get_queryset(self):
        requester_club = self.request.user.club
        return Player.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        requester_club = self.request.user.club
        serializer.save(club=requester_club)
