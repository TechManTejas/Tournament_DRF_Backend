from django.db import models
from club.models import Club

class News(models.Model):
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
