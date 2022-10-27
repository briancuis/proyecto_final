from django import forms
from mi_app.models import familiares, futbolistas, Autos

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = familiares
    fields = ['nombre', 'direccion', 'edad']

class FutbolistasForm(forms.ModelForm):
  class Meta:
    model = futbolistas
    fields = ['nombre', 'edad', 'equipo']
  
class AutosForm(forms.ModelForm):
  class Meta:
    model = Autos
    fields = ['modelo', 'marca', 'año']



