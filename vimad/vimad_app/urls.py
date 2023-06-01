from django.urls import path
from . import views
from django.urls import re_path
from django.contrib.auth import views as auth_views

app_name = 'vimad'
urlpatterns = [

    path('', views.index, name='index'),
    #path('cortos/', views.cortos, name='cortos'),
    path('perfil/', views.perfil, name='perfil'),
    path('sesion/', views.sesion, name='sesion'),
    path('video/<slug:slug>/', views.video, name='video'),
    path('ficha/<slug:slug>/', views.ficha, name='ficha'),
    path('login/', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),
    path('about/',views.about, name='about'),
    path('generos/', views.generos, name='generos'),
    path('generos/<str:genero>/', views.cortos_por_genero, name='cortos_por_genero'),
    # BARRA BUSCADORA
    path('buscar/', views.buscar, name='buscar'),

    #RESET CONTRASEÑA
    # path('reset_password/' , auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmationView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),



]
