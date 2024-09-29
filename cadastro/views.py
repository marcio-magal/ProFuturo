from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import home.views


def cadastro(request):
    if request.method == "GET":
        return render(request, 'registration/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('home')
