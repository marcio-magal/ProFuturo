from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Perfil

def cadastro(request):
    if request.method == "GET":
        return render(request, 'registration/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        imagem_perfil = request.FILES.get('imagem_perfil')  # Obtenção do arquivo de imagem

        # Verificar se já existe um usuário com o username
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        # Criar o usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        # Criar o perfil associado ao usuário
        perfil = Perfil.objects.create(user=user, imagem_perfil=imagem_perfil)
        perfil.save()

        return redirect('home')
