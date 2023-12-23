from django.db import models
from club.models import Club

class Player(models.Model):
    image = models.ImageField(upload_to='player_images/')
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    squad_number = models.PositiveIntegerField()
    # display_order = models.PositiveIntegerField()

    # STATUS_CHOICES = [
    #     ('First Eleven', 'First Eleven'),
    #     ('Substitute', 'Substitute'),
    # ]
    # status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
