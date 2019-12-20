from rest_framework import serializers
from .models import Playlist

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'spotify_user_id')
