"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_app.views import (saludo, mostrar_template, mostrar_familiares, BuscarFamiliar, AltaFamiliar, mostrar_jugadores, BuscarFutbolista, AltaFutolista,mostrar_Autos, BuscarAuto, AltaAuto)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('template/', mostrar_template),
    path('familiares/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('futbolistas/', mostrar_jugadores),
    path('futbolistas/buscar', BuscarFutbolista.as_view()),
    path('futbolista/alta', AltaFutolista.as_view()),
    path('autos/', mostrar_Autos),
    path('autos/buscar', BuscarAuto.as_view()),
    path('autos/alta', AltaAuto.as_view()),
]