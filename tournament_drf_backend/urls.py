from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user import views as user_views
from media import views as media_views
from club import views as club_views
from stadium import views as stadium_views
from team import views as team_views
from player import views as player_views
from referee import views as referee_views
from tournament import views as tournament_views
from match import views as match_views
from match import views as match_substitute_record_views
from match import views as match_card_record_views
from match import views as match_goal_record_views
from match import views as match_comment_views  # Add this line

router = DefaultRouter()
router.register('user', user_views.UserModelViewSet, basename='user')
router.register('media', media_views.MediaViewSet, basename='media')
router.register('club', club_views.ClubViewSet, basename='club')
router.register('stadium', stadium_views.StadiumViewSet, basename='stadium')
router.register('team', team_views.TeamViewSet, basename='team')
router.register('player', player_views.PlayerViewSet, basename='player')
router.register('referee', referee_views.RefereeViewSet, basename='referee')
router.register('tournament', tournament_views.TournamentViewSet, basename='tournament')
router.register('match', match_views.MatchViewSet, basename='match')
router.register('matchsubstituterecord', match_substitute_record_views.MatchSubstituteRecordViewSet, basename='matchsubstituterecord')
router.register('matchcardrecord', match_card_record_views.MatchCardRecordViewSet, basename='matchcardrecord')
router.register('matchgoalrecord', match_goal_record_views.MatchGoalRecordViewSet, basename='matchgoalrecord')
router.register('matchcomment', match_comment_views.MatchCommentViewSet, basename='matchcomment')  # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', user_views.CustomObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
