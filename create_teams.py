# create_teams.py

import os
import sys
import django
from django.core.files.base import ContentFile
import random

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tournament_drf_backend.settings')  # Replace 'your_project' with your actual project name

django.setup()

from player.models import Player
from team.models import TeamRecord
from club.models import Club
from tournament.models import Tournament

def create_teams():
    # Assuming you have 100 players and 10 clubs already created
    players = Player.objects.all()[:100]  # Adjust based on your actual method to retrieve players
    clubs = Club.objects.all()[:10]  # Adjust based on your actual method to retrieve clubs
    tournament = Tournament.objects.first()  # Assuming you have at least one tournament

    # Read the team logo file
    logo_path = 'team.jpeg'
    with open(logo_path, 'rb') as logo_file:
        logo_data = logo_file.read()

    # Create 10 teams
    for i in range(1, 11):
        team = TeamRecord(
            club=random.choice(clubs),
            tournament=tournament,
            verified=True,  # Adjust as needed
            logo=ContentFile(logo_data, name='team.jpeg'),
            name=f'Team {i}',
            short_name=f'T{i}',
            playing_player_1=random.choice(players),
            playing_player_2=random.choice(players),
            playing_player_3=random.choice(players),
            playing_player_4=random.choice(players),
            playing_player_5=random.choice(players),
            playing_player_6=random.choice(players),
            playing_player_7=random.choice(players),
            playing_player_8=random.choice(players),
            playing_player_9=random.choice(players),
            playing_player_10=random.choice(players),
            playing_player_11=random.choice(players),
            substitute_player_1=random.choice(players),
            substitute_player_2=random.choice(players),
            substitute_player_3=random.choice(players),
            substitute_player_4=random.choice(players),
            substitute_player_5=random.choice(players),
            save_team=True,  # Adjust as needed
        )
        team.save()

    print('Teams created successfully!')

if __name__ == "__main__":
    create_teams()
