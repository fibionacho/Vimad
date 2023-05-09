from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .models import Estudio
from .models import Actor
from .models import Director
from .models import Corto

# Create your views here.

#index - LISTADO DE CORTOS
def index(request):
    cortos = Corto.objects.all()
    return render(request, 'vimad_app/index.html', {'cortos': cortos})

#inicio
def inicio(request):
    return render(request, 'vimad_app/inicio.html')

#cortos - LISTADO DE CORTOS POR GENERO, IDIOMA, etc
def cortos(request, genero=None):
    cortos_drama = Corto.objects.filter(genero='drama')
    cortos_animacion = Corto.objects.filter(genero='animacion')
    cortos_espanol = Corto.objects.filter(idioma='español')
    return render(request, 'vimad_app/cortos.html', {'cortos_drama': cortos_drama, 'cortos_animacion': cortos_animacion, 'cortos_espanol': cortos_espanol})

#perfil
def perfil(request):
    return render(request, 'vimad_app/perfil.html')

#sesion
def sesion(request):
    return render(request, 'vimad_app/sesion.html')

#video
def video(request):
    return render(request, 'vimad_app/video.html')

#ficha - USO DE MODELOS COGIENDO slug POR URL
def ficha(request, slug):
    corto = get_object_or_404(Corto, slug=slug)
    directores = corto.director.all()
    actores = corto.actor.all()
    estudio = corto.estudio

    context = {
        'corto': corto,
        'directores': directores,
        'actores': actores,
        'estudio': estudio
    }

    return render(request, 'vimad_app/ficha.html', context)