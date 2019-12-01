from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlaylistSerializer
from .models import Playlist
from django.http import HttpResponse

def home(request):
    return render(request, 'api/home.html')
    
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer
