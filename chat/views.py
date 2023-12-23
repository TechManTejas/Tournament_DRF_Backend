from rest_framework import viewsets
from .models import ChatSupport, ChatClub
from .serializers import ChatSupportSerializer, ChatClubSerializer

class ChatSupportViewSet(viewsets.ModelViewSet):
    queryset = ChatSupport.objects.all()
    serializer_class = ChatSupportSerializer

class ChatClubViewSet(viewsets.ModelViewSet):
    queryset = ChatClub.objects.all()
    serializer_class = ChatClubSerializer
