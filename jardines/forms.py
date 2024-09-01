from django import forms
from .models import Jardin

class JardinForm(forms.ModelForm):
    class Meta:
        model = Jardin
        fields = ['nombre', 'estado', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2}),
        }
