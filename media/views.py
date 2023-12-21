from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import Media
from .serializers import MediaSerializer

class MediaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name', '^type', '^category', 'user__username'] 
    pagination_class = MediaPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
