from django import forms
from .models import Pagina, Perfil, Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']
        
class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'contenido']
