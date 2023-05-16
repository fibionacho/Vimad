from django.shortcuts import render,  get_object_or_404, redirect
from django.http import JsonResponse
from .models import Corto 
from django.db.models import Q

# Create your views here.

#index - LISTADO DE CORTOS
def index(request):
    cortos = Corto.objects.all().order_by('-fecha_pagina')
    return render(request, 'vimad_app/index.html', {'cortos': cortos})

#inicio
def inicio(request):
    return render(request, 'vimad_app/inicio.html')

#register
def register(request):
    return render(request, 'vimad_app/register.html')

#cortos - LISTADO DE CORTOS POR GENERO, IDIOMA, etc
def cortos(request, genero=None):
    cortos_drama = list(Corto.objects.filter(genero='drama').order_by('?'))
    cortos_animacion = list(Corto.objects.filter(genero='animacion').order_by('?'))
    cortos_espanol = list(Corto.objects.filter(idioma='español').order_by('?'))
    return render(request, 'vimad_app/cortos.html', {'cortos_drama': cortos_drama, 'cortos_animacion': cortos_animacion, 'cortos_espanol': cortos_espanol})

#perfil
def perfil(request):
    return render(request, 'vimad_app/perfil.html')

#sesion
def sesion(request):
    return render(request, 'vimad_app/sesion.html')

#video
def video(request, slug):
    if slug is None:
        return redirect('vimad:index')
    
    corto = get_object_or_404(Corto, slug=slug)
    return render(request, 'vimad_app/video.html', {'video_url': corto.video.url})


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


#BUSCADOR

def buscar(request):
    query = request.GET.get('q', '')
    cortos = Corto.objects.filter(
        Q(titulo__icontains=query) |
        Q(genero__icontains=query) |
        Q(idioma__icontains=query) |
        Q(pais__icontains=query)
    )

    cortos_list = []
    for corto in cortos:
        cortos_list.append({
            'id': corto.id,
            'titulo': corto.titulo,
            'genero': corto.genero,
            'idioma': corto.idioma,
            'pais': corto.pais,
            'imagen': corto.imagen.url,
            'slug': corto.slug,
        })

    return JsonResponse({'cortos': cortos_list})