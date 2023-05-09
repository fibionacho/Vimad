from django.shortcuts import render,  get_object_or_404
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

#cortos
def cortos(request):
    return render(request, 'vimad_app/cortos.html')

#perfil
def perfil(request):
    return render(request, 'vimad_app/perfil.html')

#sesion
def sesion(request):
    return render(request, 'vimad_app/sesion.html')

#video
def video(request):
    return render(request, 'vimad_app/video.html')



#pruebas

#ficha2 - PRUEBA INCIAL SIN USAR MODELOS
# def ficha2(request):
#     return render(request, 'vimad_app/ficha2.html')

#ficha2 - USO DE MODELOS PARA UNA FICHA UNICA
# def ficha2(request):
#     corto = Corto.objects.get(id=1)  
#     context_dict = {'corto': corto}  
#     return render(request, 'vimad_app/ficha2.html', context=context_dict)

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