from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudio
from .models import Actor
from .models import Director
from .models import Corto

# Create your views here.

#ficha1
def ficha1(request):
    return render(request, 'vimad_app/ficha1.html')

#index
def index(request):
    return render(request, 'vimad_app/index.html')

#inicio
def inicio(request):
    return render(request, 'vimad_app/inicio.html')

#otroperfil
def otroperfil(request):
    return render(request, 'vimad_app/otroperfil.html')

#peliculas
def peliculas(request):
    return render(request, 'vimad_app/peliculas.html')

#perfil
def perfil(request):
    return render(request, 'vimad_app/perfil.html')

#sesion
def sesion(request):
    return render(request, 'vimad_app/sesion.html')

#video
def video(request):
    return render(request, 'vimad_app/video.html')

    