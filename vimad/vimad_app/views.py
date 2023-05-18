from django.shortcuts import render,  get_object_or_404, redirect
from django.http import JsonResponse
from .models import Corto
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# index - LISTADO DE CORTOS


def index(request):
    cortos = Corto.objects.all().order_by('-id')
    return render(request, 'vimad_app/index.html', {'cortos': cortos})

# cortos - LISTADO DE CORTOS POR GENERO, IDIOMA, etc


def cortos(request, genero=None):
    cortos_drama = list(Corto.objects.filter(genero='drama').order_by('?'))
    cortos_animacion = list(Corto.objects.filter(
        genero='animacion').order_by('?'))
    cortos_espanol = list(Corto.objects.filter(idioma='español').order_by('?'))
    return render(request, 'vimad_app/cortos.html', {'cortos_drama': cortos_drama, 'cortos_animacion': cortos_animacion, 'cortos_espanol': cortos_espanol})

# perfil


def perfil(request):
    return render(request, 'vimad_app/perfil.html')

# sesion


def sesion(request):
    return render(request, 'vimad_app/sesion.html')

# video


def video(request, slug):
    corto = get_object_or_404(Corto, slug=slug)
    if not corto.video:
        return redirect('vimad:index')
    return render(request, 'vimad_app/video.html', {'video_url': corto.video.url})

# ficha - USO DE MODELOS COGIENDO slug POR URL


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

# BUSCADOR


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

# register


def register(request):
    if request.method == 'GET':
        return render(request, 'vimad_app/register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('vimad:index')
            except IntegrityError:
                return render(request, 'vimad_app/register.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists',
                })
        return render(request, 'vimad_app/register.html', {
            'form': UserCreationForm,
            "error": 'Password do not match',
        })

# login


def inicio(request):
    if request.method == 'GET':
        return render(request, 'vimad_app/inicio.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'vimad_app/inicio.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('vimad:index')

# logout


def signout(request):
    logout(request)
    return redirect('vimad:inicio')
