from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from playList.models import Playlist, Video
from django.http import JsonResponse

#@login_required
def index(request):
    # Filtra apenas vídeos visíveis e ordena conforme necessário
    video_list = Video.objects.filter(visibilidade=True).order_by('id')
    playlists = Playlist.objects.all()

    # Recupera a playlist "Todos os vídeos" pelo nome
    all_videos_playlist = get_object_or_404(Playlist, name="Todos os vídeos")

    # Cria o objeto Paginator e obtém os vídeos da página solicitada
    paginator = Paginator(video_list, 20)  # Carregar 20 vídeos por página
    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    # Passa a playlist "Todos os vídeos" junto com outros dados para o template
    return render(request, 'index.html', {
        'playlists': playlists,
        'videos': videos,
        'all_videos_playlist': all_videos_playlist
    })


@login_required
def adm(request):
    return render(request, 'adm.html')


@login_required
def cadastrar_video(request):
    if request.method == 'POST':
        title = request.POST.get('nome')
        url = request.POST.get('link')
        description = request.POST.get('descricao')

        # Verifica se já existe um vídeo com o mesmo título ou URL
        if Video.objects.filter(title=title).exists() or Video.objects.filter(url=url).exists():
            return JsonResponse({'error': 'Este vídeo já foi cadastrado.'})

        # Cria o novo vídeo caso não exista duplicidade
        Video.objects.create(title=title, url=url, description=description)
        return JsonResponse({'message': 'Cadastro realizado com sucesso! O vídeo estará disponível após a aprovação do administrador. Obrigado pela contribuição.'})

    return JsonResponse({'error': 'Método de requisição inválido.'})
