from django.urls import path
from . import views
from django.urls import re_path

app_name = 'vimad'
urlpatterns = [
    path('login/', views.inicio, name='inicio'),
    path('ficha1/', views.ficha1, name='ficha1'),
    path('indice/', views.index, name='index'),
    path('otroperfil/', views.otroperfil, name='otroperfil'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('perfil/', views.perfil, name='perfil'),
    path('sesion/', views.sesion, name='sesion'),
    path('video/', views.video, name='video'),
]