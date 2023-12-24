from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
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
        return TeamRecord.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        serializer.save(club=self.request.user.club)
