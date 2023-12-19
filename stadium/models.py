from django.db import models
from club.models import Club
from media.models import Media

class Stadium(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name
