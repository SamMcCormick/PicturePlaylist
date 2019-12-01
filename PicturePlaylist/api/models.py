from django.db import models

class Playlist(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    spotify_user_id = models.CharField(max_length=50)

    def __str__(self):
        return self.id
