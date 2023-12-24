from django.db import models
from club.models import Club
from player.models import Player
from tournament.models import Tournament

class TeamRecord(models.Model):
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    verified = models.BooleanField(default=False)
    
    logo = models.ImageField(upload_to='team_logos/')  
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    
    # Foreign Keys to Player model for playing players
    playing_player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_1')
    playing_player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_2')
    playing_player_3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_3')
    playing_player_4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_4')
    playing_player_5 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_5')
    playing_player_6 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_6')
    playing_player_7 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_7')
    playing_player_8 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_8')
    playing_player_9 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_9')
    playing_player_10 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_10')
    playing_player_11 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playing_player_11')

    # Foreign Keys to Player model for substitute players
    substitute_player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitute_player_1')
    substitute_player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitute_player_2')
    substitute_player_3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitute_player_3')
    substitute_player_4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitute_player_4')
    substitute_player_5 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitute_player_5')

    # New boolean attribute
    save_team = models.BooleanField(default=False)

    def __str__(self):
        return f"Team Record {self.id}"
