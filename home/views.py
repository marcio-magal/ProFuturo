from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from playList.models import Playlist, Video

@login_required
def index(request):
    videos = Video.objects.all()
    playlists = Playlist.objects.all()
    return render(request, 'index.html', {'playlists': playlists, 'videos': videos})

@login_required
def adm(request):
    return render(request, 'adm.html')
