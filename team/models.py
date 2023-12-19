from django.db import models
from club.models import Club
from media.models import Media

class Team(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    logo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
