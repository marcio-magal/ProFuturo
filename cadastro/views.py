from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def cadastro(request):
    return render(request, 'registration/cadastro.html')
