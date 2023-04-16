from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudio
from .models import Actor
from .models import Director
from .models import Corto


# Create your views here.
def index(request):
    estudio = Estudio.objects.all()
    context = {'EstudioT':estudio}
    return render(request, 'app_noticias/listado.html', context)


def detalle_noticias(request, titulo):
    NoticiasO = Noticias.objects.get(titulo=titulo)
    context = {'NoticiasT':NoticiasO}
    return render(request, 'app_noticias/noticias.html', context)
