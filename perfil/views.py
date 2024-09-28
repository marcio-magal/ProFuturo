from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def editar(request):
    return render(request, 'editar-perfil.html')
