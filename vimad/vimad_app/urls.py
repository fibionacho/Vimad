from django.urls import path
from . import views

app_name = 'vimad'
urlpatterns = [
    path('login', views.inicio, name='inicio'),
    path('ficha1', views.ficha1, name='ficha1'),
    path('ficha2', views.ficha2, name='ficha2'),
    path('inicio', views.inicio, name='inicio'),
    path('otroperfil', views.otroperfil, name='otroperfil'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('perfil', views.perfil, name='perfil'),
    path('series', views.series, name='series'),
    path('sesion', views.sesion, name='sesion'),
    path('video', views.video, name='video'),
]