from django.conf import settings
from django.contrib import admin
from home.views import index
from cadastro.views import cadastro
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cadastro/', cadastro),
    path('perfil/', include('perfil.urls')),
    path('playlist/', include('playList.urls')),

    path('accounts/', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
