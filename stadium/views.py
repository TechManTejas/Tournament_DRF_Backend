from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import Stadium
from .serializers import StadiumReadSerializer, StadiumWriteSerializer


class StadiumPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["^name"]
    pagination_class = StadiumPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StadiumReadSerializer
        elif self.request.method in ["POST", "PUT", "PATCH"]:
            return StadiumWriteSerializer

    def perform_create(self, serializer):
        serializer.save(club=self.request.user.club)
