from django.db import models
from club.models import Club

class GameMode(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='game_mode_images/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Tournament(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
    logo = models.ImageField(upload_to='tournament_logos/')
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50)
    start_time = models.TimeField()
    start_date = models.DateField()
    no_of_teams = models.PositiveIntegerField(default=0, blank=True, null=True)
    no_of_groups = models.PositiveIntegerField(default=0, blank=True, null=True)
    playing_time = models.PositiveIntegerField()  # in minutes
    pause_between_games = models.PositiveIntegerField()  # in minutes
    points_draw = models.PositiveIntegerField(blank=True, null=True)
    points_winner = models.PositiveIntegerField(blank=True, null=True)
    points_defeat = models.PositiveIntegerField(blank=True, null=True)

    TIMER_CHOICES = [
        ('up', 'Runs Up'),
        ('down', 'Runs Down'),
    ]
    timer = models.CharField(max_length=4, choices=TIMER_CHOICES)

    # New attribute 'status'
    status = models.CharField(max_length=20, default='Not Started')

    # Updated attribute 'game_mode' as a foreign key
    game_mode = models.ForeignKey(GameMode, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
