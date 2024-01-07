from django.db import models
from club.models import Club
from group.models import Group, GroupTeam
from round.models import Round
from team.models import TeamRecord
from tournament.models import Tournament
from referee.models import Referee
from stadium.models import Stadium
from player.models import Player
from django.utils import timezone


class Match(models.Model):
    teamA = models.ForeignKey(GroupTeam, on_delete=models.CASCADE, related_name="teamA")
    teamB = models.ForeignKey(GroupTeam, on_delete=models.CASCADE, related_name="teamB")

    jersey_color_A = models.CharField(max_length=50, blank=True)
    jersey_color_B = models.CharField(max_length=50, blank=True)

    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True, blank=True)

    referee_head = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE, 
        related_name="head_referee_matches", 
        null=True, 
        blank=True
    )
    referee_assistant = models.ForeignKey(
        Referee,
        on_delete=models.CASCADE,
        related_name="assistant_referee_matches",
        null=True,
        blank=True,
    )
    referee_assistant_2 = models.ForeignKey(
        Referee,
        on_delete=models.CASCADE,
        related_name="assistant_referee_2_matches",
        null=True,
        blank=True,
    )
    referee_assistant_3 = models.ForeignKey(
        Referee,
        on_delete=models.CASCADE,
        related_name="assistant_referee_3_matches",
        null=True,
        blank=True,
    )
    
    start_time = models.TimeField(null=True, blank=True)
    timer = models.CharField(max_length=4, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    status = models.CharField(max_length=255, default="scheduled", blank=True)

    id = models.CharField(primary_key=True, max_length=255)

    def __str__(self):
        return f"{self.teamA} vs {self.teamB}"


class MatchSubstituteRecord(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="substitute_records_in")
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="substitute_records_out")
    minute = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.match} - {self.player_in} in, {self.player_out} out at {self.minute} minutes"


class MatchCardRecord(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="card_records"
    )

    CARD_TYPE_CHOICES = [
        ("red", "Red"),
        ("yellow", "Yellow"),
        ("time", "Time"),
    ]
    card_type = models.CharField(max_length=6, choices=CARD_TYPE_CHOICES)

    penalty_time = models.PositiveIntegerField(blank=True, null=True)
    minute = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.match} - {self.player} - {self.card_type} card at {self.minute} minutes"


class MatchGoalRecord(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="goal_records")
    goal_minute = models.PositiveIntegerField()
    is_penalty_goal = models.BooleanField(default=False)
    is_own_goal = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.match} - {self.player} - Goal at {self.goal_minute} minutes"


class MatchComment(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    comment_minute = models.PositiveIntegerField()
    comment = models.TextField()

    COMMENT_TYPE_CHOICES = [
        ("normal", "Normal"),
        ("goal", "Goal"),
        ("substitution", "Substitution"),
        ("card", "Card"),
        ("other", "Other"),
    ]
    type = models.CharField(
        max_length=15, choices=COMMENT_TYPE_CHOICES, default="normal"
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.match} - {self.comment} at {self.comment_minute} minutes"
