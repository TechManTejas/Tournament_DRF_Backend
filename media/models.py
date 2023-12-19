from django.db import models
from user.models import User

class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media_images/')
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
