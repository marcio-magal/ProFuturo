from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem_perfil = models.ImageField(upload_to='perfil_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username
