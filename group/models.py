from django.db import models
from club.models import Club
from team.models import TeamRecord
from round.models import Round  

class Group(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    team_records = models.ManyToManyField(TeamRecord, related_name='groups')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
