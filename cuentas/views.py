from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Pagina, Perfil, Mensaje
from .forms import PaginaForm, PerfilForm, MensajeForm

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()
    
    return render(request, 'cuentas/enviar_mensaje.html', {'form': form})

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    mensajes_enviados = Mensaje.objects.filter(emisor=request.user).order_by('-fecha_envio')
    
    return render(request, 'cuentas/bandeja_entrada.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados
    })

@login_required
def ver_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'cuentas/ver_perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'cuentas/editar_perfil.html', {'form': form})

def acerca_de_mi(request):
    return render(request, 'cuentas/acerca_de_mi.html')

def inicio(request):
    return render(request, 'cuentas/inicio.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

@login_required
def crear_pagina(request):
    if request.method == 'POST':
        form = PaginaForm(request.POST)
        if form.is_valid():
            nueva_pagina = form.save(commit=False)
            nueva_pagina.autor = request.user
            nueva_pagina.save()
            return redirect('ver_paginas')
    else:
        form = PaginaForm()
    return render(request, 'cuentas/crear_pagina.html', {'form': form})

def ver_paginas(request):
    paginas = Pagina.objects.all()
    return render(request, 'cuentas/ver_paginas.html', {'paginas': paginas})

@login_required
def editar_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    if request.user != pagina.autor:
        return redirect('ver_paginas')
    
    if request.method == 'POST':
        form = PaginaForm(request.POST, instance=pagina)
        if form.is_valid():
            form.save()
            return redirect('ver_paginas')
    else:
        form = PaginaForm(instance=pagina)
    return render(request, 'cuentas/editar_pagina.html', {'form': form})

@login_required
def eliminar_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    if request.user != pagina.autor:
        return redirect('ver_paginas')

    if request.method == 'POST':
        pagina.delete()
        return redirect('ver_paginas')
    return render(request, 'cuentas/eliminar_pagina.html', {'pagina': pagina})