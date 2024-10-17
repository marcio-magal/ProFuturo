from django.contrib import admin
from .models import Video, Playlist, PlaylistVideo

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')
    search_fields = ('title', 'url')
    list_filter = ('created_at',)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(PlaylistVideo)
class PlaylistVideoAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'video', 'order')
    list_filter = ('playlist',)
