from django.shortcuts import render

# Create your views here.
def perfil(request):
    return render(request, 'perfil.html')

def editar(request):
    return render(request, 'editar-perfil.html')
