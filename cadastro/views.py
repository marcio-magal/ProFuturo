from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil

def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        imagem_perfil = request.FILES.get('imagem_perfil')

        # Verificar se já existe um usuário com o username
        if User.objects.filter(username=username).exists():
            error_message = "Já existe um usuário com esse username."
            return render(request, 'registration/cadastro.html', {'error': error_message})

        # Criar o usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        # Criar o perfil associado ao usuário
        perfil = Perfil.objects.create(user=user, imagem_perfil=imagem_perfil)
        perfil.save()

        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('home')

    return render(request, 'registration/cadastro.html')
