# create_players.py

import os
import sys
import django
from django.core.files.base import ContentFile

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tournament_drf_backend.settings')  # Replace 'your_project' with your actual project name

django.setup()

from player.models import Player
from club.models import Club

def create_players():
    # Read the image file
    image_path = 'player.jpg'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Assuming you have 100 clubs already created, adjust this as needed
    clubs = Club.objects.all()  # Adjust based on your actual method to retrieve clubs

    # Create 100 player objects
    for i in range(1, 101):
        random_club = clubs.order_by('?').first()  # Randomly select a club

        # Use ContentFile to create a file-like object
        image_content = ContentFile(image_data, name='player.jpg')

        player = Player(
            image=image_content,
            club=random_club,
            name=f'Player{i}',
            squad_number=i,
        )
        player.save()

    print('Players created successfully!')

if __name__ == "__main__":
    create_players()
