from django.db import models

class Club(models.Model):
    logo = models.ImageField(upload_to='club_logos/') 
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
