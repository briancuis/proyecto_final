from django.http import HttpResponse
from django.shortcuts import render
from mi_app.models import familiares
# Create your views here.


def saludo(request):
    return HttpResponse("HOLA BOBO")


def mostrar_template(request):
    return render(request, 'mi_app/index.html')

def mostrar_familiares(request):
    lista_familiares = familiares.objects.all()
    return render(request, "mi_app/familiares.html", 
                {"lista_familiares": lista_familiares})