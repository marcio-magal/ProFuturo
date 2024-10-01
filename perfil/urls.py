from django.urls import path
from . import views
urlpatterns = [
    path('', views.perfil, name='perfil'),
    path('editar/', views.editar, name='editar'),
]
