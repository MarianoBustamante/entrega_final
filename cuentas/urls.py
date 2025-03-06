from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect
from .views import iniciar_sesion, cerrar_sesion
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('crear_pagina/', views.crear_pagina, name='crear_pagina'),
    path('ver_paginas/', views.ver_paginas, name='ver_paginas'),
    path('editar_pagina/<int:pk>/', views.editar_pagina, name='editar_pagina'),
    path('eliminar_pagina/<int:pk>/', views.eliminar_pagina, name='eliminar_pagina'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('bandeja_entrada/', views.bandeja_entrada, name='bandeja_entrada'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]