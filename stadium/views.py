from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from stadium.serializers import StadiumSerializer
from .models import Stadium


class StadiumPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    filter_backends = [SearchFilter]
    search_fields = ["^name"]
    pagination_class = StadiumPagination

    def get_queryset(self):
        requester_club = self.request.user.club
        return Stadium.objects.filter(club=requester_club)

    def perform_create(self, serializer):
        serializer.save(club=self.request.user.club)
