from django.urls import path
from . import views
from django.urls import re_path

app_name = 'vimad'
urlpatterns = [
    path('login/', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('indice/', views.index, name='index'),
    path('cortos/', views.cortos, name='cortos'),
    path('perfil/', views.perfil, name='perfil'),
    path('sesion/', views.sesion, name='sesion'),
    path('video/', views.video, name='video'),
    #path para una ficha cogiendo por slug:
    path('ficha/<slug:slug>/', views.ficha, name='ficha')
]