from rest_framework import viewsets
from .models import Referee
from .serializers import RefereeSerializer

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
