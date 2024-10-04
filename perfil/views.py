from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from cadastro.models import Perfil  # Certifique-se de importar o modelo correto
from django.core.files.storage import default_storage

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def editar(request):
    user = request.user  # Obtém o usuário logado

    try:
        perfil = Perfil.objects.get(user=user)  # Busca o perfil do usuário logado
    except Perfil.DoesNotExist:
        perfil = None  # Caso o perfil não exista, definimos como None

    if request.method == "POST":
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        nova_imagem = request.FILES.get('imagem_perfil')  # Obtém o arquivo de imagem enviado

        # Verifica se o novo username já existe e não pertence ao usuário logado
        if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            return HttpResponse('Já existe um usuário com esse username')

        # Atualiza os dados do usuário
        user.username = new_username
        user.email = new_email
        user.save()

        # Atualiza a imagem de perfil se uma nova imagem for enviada
        if nova_imagem:
            if perfil:
                # Apaga a imagem anterior se já existir
                if perfil.imagem_perfil:
                    default_storage.delete(perfil.imagem_perfil.path)
                perfil.imagem_perfil = nova_imagem
                perfil.save()
            else:
                # Cria um novo perfil se não existir
                Perfil.objects.create(user=user, imagem_perfil=nova_imagem)

        return redirect('perfil')

    return render(request, 'editar-perfil.html', {'user': user, 'perfil': perfil})
