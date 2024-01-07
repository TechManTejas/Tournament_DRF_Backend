from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user import views as user_views
from club import views as club_views
from stadium import views as stadium_views
from round import views as round_views
from group import views as group_views
from team import views as team_views
from player import views as player_views
from referee import views as referee_views
from tournament import views as tournament_views
from news import views as news_views
from match import views as match_views
from match import views as match_substitute_record_views
from match import views as match_card_record_views
from match import views as match_goal_record_views
from match import views as match_comment_views
from chat.views import ChatSupportViewSet, ChatClubViewSet  # Add these lines

router = DefaultRouter()
router.register('user-register', user_views.UserRegisterModelViewSet, basename='user-register')
router.register('user-lobby', user_views.UserLobbyModelViewSet, basename='user-lobby')
router.register('user', user_views.UserModelViewSet, basename='user')
router.register('club', club_views.ClubViewSet, basename='club')
router.register('stadium', stadium_views.StadiumViewSet, basename='stadium')
router.register('stadium-all', stadium_views.StadiumAllViewSet, basename='stadium-all')
router.register('round', round_views.RoundViewSet, basename='round')
router.register('group', group_views.GroupViewSet, basename='group')
router.register('group-team', group_views.GroupTeamViewSet, basename='group-team')
router.register('teamrecord', team_views.TeamRecordViewSet, basename='team')
router.register('player', player_views.PlayerModelViewSet, basename='player')
router.register('referee', referee_views.RefereeModelViewSet, basename='referee')
router.register('referee-all', referee_views.RefereeAllModelViewSet, basename='referee-all')
router.register('tournament', tournament_views.TournamentViewSet, basename='tournament')
router.register('match', match_views.MatchViewSet, basename='match')
router.register('matchsubstituterecord', match_substitute_record_views.MatchSubstituteRecordViewSet, basename='matchsubstituterecord')
router.register('matchcardrecord', match_card_record_views.MatchCardRecordViewSet, basename='matchcardrecord')
router.register('matchgoalrecord', match_goal_record_views.MatchGoalRecordViewSet, basename='matchgoalrecord')
router.register('matchcomment', match_comment_views.MatchCommentViewSet, basename='matchcomment')
router.register('news', news_views.NewsViewSet, basename='news')  
router.register('gamemode', tournament_views.GameModeViewSet, basename='gamemode')  
router.register('chatsupport', ChatSupportViewSet, basename='chatsupport')  
router.register('chatclub', ChatClubViewSet, basename='chatclub')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', user_views.CustomObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
