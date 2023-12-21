from django.db import models
from club.models import Club

class Team(models.Model):
    logo = models.ImageField(upload_to='team_logos/')  
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
