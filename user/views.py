from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer


class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ["^username", "^first_name", "^last_name", "^email", "^role"]
    pagination_class = UserPagination

    def get_queryset(self):
        user_club = self.request.user.club
        return User.objects.filter(club=user_club).exclude(id=self.request.user.id)

    def perform_create(self, serializer):
        user = User.objects.create_user(
            **serializer.validated_data, club=self.request.user.club
        )
        Token.objects.create(user=user)

class UserLobbyModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    http_method_names = ["post"]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": str(token.user)})


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])

        # Serialize the user object
        user_serializer = UserSerializer(token.user)
        serialized_user = user_serializer.data

        return Response({"token": token.key, "user": serialized_user})
