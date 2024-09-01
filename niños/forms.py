from django import forms
from .models import Niño
from jardines.models import Jardin


class NiñoForm(forms.ModelForm):
    class Meta:
        model = Niño
        fields = ['registro', 'nombre', 'fecha_nacimiento', 'tipo_sangre', 'ciudad_nacimiento', 'acudiente', 'telefono', 'direccion', 'eps', 'jardin']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jardin'].queryset = Jardin.get_aprobados()