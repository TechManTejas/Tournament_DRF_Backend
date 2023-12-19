from django.db import models
from club.models import Club
from media.models import Media

class Tournament(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50)
    logo = models.ForeignKey(Media, on_delete=models.CASCADE)
    points_draw = models.PositiveIntegerField()
    start_time = models.TimeField()
    start_date = models.DateField()
    no_of_teams = models.PositiveIntegerField()
    no_of_groups = models.PositiveIntegerField()
    playing_time = models.PositiveIntegerField()  # in minutes
    pause_between_games = models.PositiveIntegerField()  # in minutes
    points_winner = models.PositiveIntegerField()
    points_defeat = models.PositiveIntegerField()

    TIMER_CHOICES = [
        ('up', 'Runs Up'),
        ('down', 'Runs Down'),
    ]
    timer = models.CharField(max_length=4, choices=TIMER_CHOICES)

    def __str__(self):
        return self.name
