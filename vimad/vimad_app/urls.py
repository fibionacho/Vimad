from django.urls import path
from . import views
from django.urls import re_path

app_name = 'vimad'
urlpatterns = [

    path('', views.index, name='index'),
    path('cortos/', views.cortos, name='cortos'),
    path('perfil/', views.perfil, name='perfil'),
    path('sesion/', views.sesion, name='sesion'),
    path('video/<slug:slug>/', views.video, name='video'),
    path('ficha/<slug:slug>/', views.ficha, name='ficha'),
    path('login/', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),

# BARRA BUSCADORA
    path('buscar/', views.buscar, name='buscar'),
]
