from django.conf import settings
from django.contrib import admin
from home.views import index, adm
from cadastro.views import cadastro
from django.urls import path, include
from django.conf.urls.static import static
from playList.views import playlist_detail, like_video, video_like_status, add_comment, edit_comment, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/', adm),
    path('playlist/<int:playlist_id>/', playlist_detail, name='playlist-detail'),
    path('playlist/like/<int:video_id>/', like_video, name='like-video'),
    path('playlist/like/<int:video_id>/status/', video_like_status, name='video-like-status'),
    path('playlist/comment/add/<int:video_id>/', add_comment, name='add-comment'),
    path('playlist/comment/edit/<int:comment_id>/', edit_comment, name='edit-comment'),
    path('playlist/comment/delete/<int:comment_id>/', delete_comment, name='delete-comment'),
    path('', index, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', include('perfil.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
