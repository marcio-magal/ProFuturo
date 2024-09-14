from django.urls import path
from . import views
urlpatterns = [
    path('', views.perfil),
    path('editar/', views.editar)
]
