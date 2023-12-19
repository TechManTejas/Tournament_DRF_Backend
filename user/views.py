from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        
        user = token.user
        user_type = None

        if hasattr(user, 'club_admin'):
            user_type = 'club_admin'     
        elif hasattr(user, 'club_user'):
            user_type = 'club_user'
            
        response.data['user_type'] = user_type
        
        return response
