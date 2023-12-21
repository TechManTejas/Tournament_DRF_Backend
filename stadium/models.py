from django.db import models
from club.models import Club

class Stadium(models.Model):
    image = models.ImageField(upload_to='stadium_images/') 
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
