from django.db import models
from media.models import Media

class Club(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name
