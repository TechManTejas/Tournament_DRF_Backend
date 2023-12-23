from django.db import models
from tournament.models import Tournament  
from club.models import Club

class Round(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    schedule = models.JSONField(default=list)  
    result = models.JSONField(default=list)   

    def __str__(self):
        return f"{self.tournament.name} - Round {self.name} ({self.club.name})"
