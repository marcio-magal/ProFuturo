from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from playList.models import Playlist
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Video, VideoLike, Comment

@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    videos = playlist.videos.filter(visibilidade=True)  # Filtra apenas vídeos visíveis
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


@login_required
@require_POST
def add_comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    text = request.POST.get('text', '').strip()

    if text:
        comment = Comment.objects.create(user=request.user, video=video, text=text)
        return JsonResponse({'id': comment.id, 'user': comment.user.username, 'text': comment.text, 'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')})
    return JsonResponse({'error': 'Texto do comentário não pode estar vazio'}, status=400)

@login_required
@require_POST
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    text = request.POST.get('text', '').strip()

    if text:
        comment.text = text
        comment.save()
        return JsonResponse({'id': comment.id, 'text': comment.text, 'updated_at': comment.updated_at.strftime('%Y-%m-%d %H:%M:%S')})
    return JsonResponse({'error': 'Texto do comentário não pode estar vazio'}, status=400)

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return JsonResponse({'success': True})
