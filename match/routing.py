from django.urls import re_path

from .consumers import ScoreCardConsumer

websocket_urlpatterns = [
    re_path(r'ws/scorecard/(?P<match_id>\w+)/$', ScoreCardConsumer.as_asgi()),
]
