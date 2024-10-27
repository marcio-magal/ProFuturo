from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from playList.models import Playlist
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Video, VideoLike

@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    videos = playlist.videos.all()
    return render(request, 'playlist.html', {'playlist': playlist, 'videos': videos})


@login_required
def video_like_status(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    liked = VideoLike.objects.filter(user=request.user, video=video).exists()

    return JsonResponse({'liked': liked, 'likes': video.likes})

@login_required
@require_POST
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    liked = VideoLike.objects.filter(user=request.user, video=video).exists()

    if liked:
        # Descurtir se já curtiu
        VideoLike.objects.filter(user=request.user, video=video).delete()
        video.likes = max(0, video.likes - 1)
        video.save()
        return JsonResponse({'liked': False, 'likes': video.likes})
    else:
        # Curtir se ainda não curtiu
        VideoLike.objects.create(user=request.user, video=video)
        video.likes += 1
        video.save()
        return JsonResponse({'liked': True, 'likes': video.likes})
