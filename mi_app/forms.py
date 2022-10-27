from django import forms
from mi_app.models import familiares

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = familiares
    fields = ['nombre', 'direccion', 'edad']


