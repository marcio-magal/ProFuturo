from django.conf import settings
from django.contrib import admin
from home.views import index, adm
from playList.views import playList
from cadastro.views import cadastro
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/', adm),
    path('playlist/', playList),
    path('', index, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', include('perfil.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
