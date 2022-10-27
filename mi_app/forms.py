from django import forms
from mi_app.models import familiares, futbolista

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = familiares
    fields = ['nombre', 'direccion', 'edad']


class FutbolistaForm(forms.ModelForm):
  class Meta:
    model = futbolista
    fields = ['nombre', 'edad', 'equipo']