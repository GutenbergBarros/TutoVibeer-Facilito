from django.conf.urls import url

from . import views

app_name = 'music'
urlpatterns = [
    #url(r'^music/')
    #/music/

    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


    url(r'^registrar/$', views.RegistroUsuario.as_view(), name='registrar'),

    # /music/<album_id>/favorite/

#    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/

    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/

    url(r'album(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),



]