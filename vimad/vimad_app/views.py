from django.shortcuts import render,  get_object_or_404, redirect
from django.http import JsonResponse
from .models import Corto
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, CustomAuthenticationForm


# index - LISTADO DE CORTOS INICIAL - LISTADO DE CORTOS POR GENERO, IDIOMA, etc

def index(request, genero=None, idioma=None):
    cortos = Corto.objects.all().order_by('-id')[:10]
    cortos_animacion = list(Corto.objects.filter(genero='animacion').order_by('?'))[:10]
    cortos_espanol = list(Corto.objects.filter(idioma='español').order_by('?'))[:10]
    return render(request, 'vimad_app/index.html', {'cortos': cortos, 'cortos_animacion': cortos_animacion, 'cortos_espanol': cortos_espanol})

# cortos - LISTADO DE CORTOS POR GENERO, IDIOMA, etc


def cortos(request, genero=None, idioma=None):
    cortos_drama = list(Corto.objects.filter(genero='drama').order_by('?'))[:10]
    cortos_animacion = list(Corto.objects.filter(
        genero='animacion').order_by('?'))[:10]
    cortos_espanol = list(Corto.objects.filter(idioma='español').order_by('?'))[:10]
    return render(request, 'vimad_app/cortos.html', {'cortos_drama': cortos_drama, 'cortos_animacion': cortos_animacion, 'cortos_espanol': cortos_espanol})

# perfil


@login_required(login_url='vimad:inicio')
def perfil(request):
    return render(request, 'vimad_app/perfil.html')

# sesion


@login_required(login_url='vimad:inicio')
def sesion(request):
    return render(request, 'vimad_app/sesion.html')

# video


@login_required(login_url='vimad:inicio')
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
    if request.user.is_authenticated:
        return redirect('vimad:index')
    else:
        if request.method == 'GET':
            return render(request, 'vimad_app/register.html', {
                'form': CreateUserForm
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
                        'form': CreateUserForm,
                        "error": 'El usuario ya existe',
                    })
            return render(request, 'vimad_app/register.html', {
                'form': CreateUserForm,
                "error": 'Las contraseñas no coinciden',
            })

# login


def inicio(request):
    if request.user.is_authenticated:
        return redirect('vimad:index')
    else:
        if request.method == 'GET':
            return render(request, 'vimad_app/inicio.html', {
                'form': CustomAuthenticationForm
            })
        else:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'vimad_app/inicio.html', {
                    'form': CustomAuthenticationForm,
                    'error': 'Usuario o contraseña incorrectos'
                })
            else:
                login(request, user)
                return redirect('vimad:index')

# logout


def signout(request):
    logout(request)
    return redirect('vimad:inicio')


# about

def about(request):
    return render(request, 'vimad_app/about.html')


# pruebas 

def generos(request):
    generos = Corto.objects.values_list('genero', flat=True).distinct()
    return render(request, 'vimad_app/generos.html', {'generos': generos})

def cortos_por_genero(request, genero):
    cortos = Corto.objects.filter(genero=genero)
    return render(request, 'vimad_app/cortos_por_genero.html', {'cortos': cortos})