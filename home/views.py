from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from playList.models import Playlist, Video

@login_required
def index(request):
    # Ordene os vídeos por uma coluna específica, como 'id', 'created_at' ou 'title'.
    video_list = Video.objects.all().order_by('id')
    playlists = Playlist.objects.all()

    # Crie o objeto Paginator e obtenha os vídeos da página solicitada
    paginator = Paginator(video_list, 12)  # Carregar 12 vídeos por página
    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    return render(request, 'index.html', {'playlists': playlists, 'videos': videos})

@login_required
def adm(request):
    return render(request, 'adm.html')
