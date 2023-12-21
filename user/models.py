from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('club_admin', 'Club Admin'),
        ('club_user', 'Club User'),
    ]

    club = models.ForeignKey('club.Club', on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLES, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
