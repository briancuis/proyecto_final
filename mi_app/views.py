from django.http import HttpResponse
from django.shortcuts import render
from mi_app.models import familiares, futbolistas, Autos
from mi_app.forms import Buscar, FamiliarForm, FutbolistasForm, AutosForm
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

def mostrar_jugadores(request):
    lista_futbolistas = futbolistas.objects.all()
    return render(request, "mi_app/futbolistas.html",
                {"lista_futbolistas": lista_futbolistas})

def mostrar_Autos(request):
    lista_Autos = Autos.objects.all()
    return render(request, "mi_app/autos.html",
                {"lista_Autos": lista_Autos})

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

class BuscarFutbolista(View):

    form_class = Buscar
    template_name = 'mi_app/buscar_futbolista.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_futbolistas = futbolistas.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_futbolistas':lista_futbolistas})
        return render(request, self.template_name, {"form": form})


class AltaFutolista(View):
    form_class = FutbolistasForm
    template_name = 'mi_app/alta_futbolista.html'
    initial = {"nombre":"", "edad":"", "equipo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})
     
class BuscarAuto(View):

    form_class = Buscar
    template_name = 'mi_app/buscar_auto.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            modelo = form.cleaned_data.get("modelo")
            lista_Autos = Autos.objects.filter(modelo__icontains=modelo).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_Autos':lista_Autos})

        return render(request, self.template_name, {"form": form})

class AltaAuto(View):
    form_class = AutosForm
    template_name = 'mi_app/alta_auto.html'
    initial = {"modelo":"", "marca":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el auto {form.cleaned_data.get('modelo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})    


