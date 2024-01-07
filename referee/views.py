from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Referee
from .serializers import RefereeSerializer

class RefereePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class RefereeModelViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    filter_backends = [SearchFilter]
    search_fields = ["^name"]
    pagination_class = RefereePagination

    def get_queryset(self):
        requester_club = self.request.user.club
        return Referee.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        requester_club = self.request.user.club
        serializer.save(club=requester_club)

class RefereeAllModelViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

    def get_queryset(self):
        requester_club = self.request.user.club
        return Referee.objects.filter(club=requester_club)

