from django.http import HttpResponse
from django.shortcuts import render
from mi_app.models import familiares, futbolista
from mi_app.forms import Buscar, FamiliarForm, FutbolistaForm
from django.views import View
# Create your views here.


def saludo(request):
    return HttpResponse("HOLA BOBO")


def mostrar_template(request):
    return render(request, 'mi_app/index.html')

def mostrar_familiares(request):
    lista_familiares = familiares.objects.all()
    return render(request, "mi_app/familiares.html", 
                {"lista_familiares": lista_familiares})

def mostrar_futbolistas(request):
    lista_jugadores = futbolista.objects.all()
    return render(request, "mi_app/f")

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'mi_app/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = familiares.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'mi_app/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class Futbolista(View):
    form_class = FutbolistaForm
