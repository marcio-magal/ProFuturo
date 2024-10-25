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

    def youtube_id(self):
        """
        Extraia o ID do vídeo do YouTube, suportando URLs padrão e encurtadas.
        """
        query = urlparse(self.url)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                return parse_qs(query.query).get("v", [None])[0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        return None

    def youtube_thumbnail(self):
        """
        Obtenha a thumbnail do YouTube.
        """
        video_id = self.youtube_id()
        if video_id:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
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
