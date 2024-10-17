from django.db import models

from urllib.parse import urlparse, parse_qs
import requests

class Video(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def youtube_thumbnail(self):
        # Extrai o ID do vídeo do YouTube a partir da URL
        query = urlparse(self.url)
        video_id = parse_qs(query.query).get("v")
        if video_id:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id[0]}/hqdefault.jpg"
            try:
                # Verifica se é possível acessar a URL da thumbnail
                response = requests.head(thumbnail_url, timeout=5)
                if response.status_code == 200:
                    return thumbnail_url
            except requests.RequestException:
                pass  # Se der erro, vai usar a imagem padrão

        # Caminho para a imagem padrão
        return "/static/img/default_video_thumbnail.jpg"


class Playlist(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    videos = models.ManyToManyField(Video, through='PlaylistVideo', related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_default_thumbnail(self):
        return '/static/img/default_playlist_thumbnail.jpeg'  # Caminho para a imagem padrão


class PlaylistVideo(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ('playlist', 'video')

    def __str__(self):
        return f"{self.video.title} in {self.playlist.name}"
