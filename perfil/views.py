from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def editar(request):
    user = request.user  # Obtém o usuário logado

    if request.method == "POST":
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')

        # Verifica se o novo username já existe e não pertence ao usuário logado
        if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            return HttpResponse('Já existe um usuário com esse username')

        # Atualiza os dados do usuário
        user.username = new_username
        user.email = new_email
        user.save()

        return redirect('perfil')

    return render(request, 'editar-perfil.html', {'user': user})
