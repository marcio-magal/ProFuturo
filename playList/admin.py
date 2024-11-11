from django.contrib import admin
from .models import Video, Playlist, PlaylistVideo, Comment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'visibilidade')
    search_fields = ('title', 'url')
    list_filter = ('created_at', 'visibilidade')

    # Define as ações customizadas
    actions = ['marcar_como_visivel', 'marcar_como_invisivel']

    # Ação para marcar vídeos como visíveis
    @admin.action(description='Mostrar vídeos selecionados')
    def marcar_como_visivel(self, request, queryset):
        queryset.update(visibilidade=True)

    # Ação para marcar vídeos como invisíveis
    @admin.action(description='Ocultar  vídeos selecionados')
    def marcar_como_invisivel(self, request, queryset):
        queryset.update(visibilidade=False)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(PlaylistVideo)
class PlaylistVideoAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'video', 'order')
    list_filter = ('playlist',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'text', 'created_at', 'updated_at')
    search_fields = ('user__username', 'text')
    list_filter = ('created_at', 'updated_at', 'video')

    # Remove a opção de edição
    def has_change_permission(self, request, obj=None):
        return False  # Desabilita edição

    # Permite apenas exclusão
    def has_delete_permission(self, request, obj=None):
        return True

    # Remove a opção de adicionar
    def has_add_permission(self, request):
        return False  # Desabilita adição
