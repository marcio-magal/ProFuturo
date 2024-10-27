from django.conf import settings
from django.contrib import admin
from home.views import index, adm
from cadastro.views import cadastro
from django.urls import path, include
from django.conf.urls.static import static
from playList.views import playlist_detail, like_video, video_like_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/', adm),
    path('playlist/<int:playlist_id>/', playlist_detail, name='playlist-detail'),
    path('playlist/like/<int:video_id>/', like_video, name='like-video'),
    path('playlist/like/<int:video_id>/status/', video_like_status, name='video-like-status'),
    path('', index, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', include('perfil.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
