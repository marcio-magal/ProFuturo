from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from playList.models import Playlist

@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    videos = playlist.videos.all()
    return render(request, 'playlist.html', {'playlist': playlist, 'videos': videos})
