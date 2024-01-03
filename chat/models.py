from django.db import models
from django.utils import timezone
from user.models import User
from club.models import Club

class ChatSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.club.name} - {self.timestamp}"

class ChatClub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Set timestamp to the current time in the 'Asia/Kolkata' time zone
        self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.club.name} - {self.timestamp}"
