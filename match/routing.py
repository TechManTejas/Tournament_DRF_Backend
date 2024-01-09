from django.urls import re_path

from .consumers import ScoreCardConsumer, MatchCardConsumer, ScheduleCardConsumer, RefereesCardConsumer, GoalScorerCardConsumer, CardsCardConsumer, FreeTextCardConsumer, SwapsCardConsumer, TimeCardConsumer

websocket_urlpatterns = [
    re_path(r'ws/scorecard/(?P<match_id>\w+)/$', ScoreCardConsumer.as_asgi()),
    re_path(r'ws/matchcard/(?P<match_id>\w+)/$', MatchCardConsumer.as_asgi()),
    re_path(r'ws/schedulecard/(?P<match_id>\w+)/$', ScheduleCardConsumer.as_asgi()),
    re_path(r'ws/refereescard/(?P<match_id>\w+)/$', RefereesCardConsumer.as_asgi()),
    re_path(r'ws/goalscorercard/(?P<match_id>\w+)/$', GoalScorerCardConsumer.as_asgi()),
    re_path(r'ws/cardscard/(?P<match_id>\w+)/$', CardsCardConsumer.as_asgi()),
    re_path(r'ws/freetextcard/(?P<match_id>\w+)/$', FreeTextCardConsumer.as_asgi()),
    re_path(r'ws/swapscard/(?P<match_id>\w+)/$', SwapsCardConsumer.as_asgi()),
    re_path(r'ws/timecard/(?P<match_id>\w+)/$', TimeCardConsumer.as_asgi()),
]
