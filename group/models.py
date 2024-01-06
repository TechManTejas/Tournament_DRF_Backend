from django.db import models
from club.models import Club
from team.models import TeamRecord
from round.models import Round
from tournament.models import Tournament  

class GroupTeam(models.Model):
    team_record = models.ForeignKey(TeamRecord, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(default=0)
    goals_pos = models.IntegerField(default=0)
    goals_neg = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Points: {self.points}, Goals Pos: {self.goals_pos}, Goals Neg: {self.goals_neg}"

class Group(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    group_team_records = models.ManyToManyField(GroupTeam, related_name='groups')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

