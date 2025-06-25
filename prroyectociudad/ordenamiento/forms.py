from django import forms
from .models import Parroquia, Barrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "ubicacion": forms.Select(attrs={"class": "form-select"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
        }

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "numero_viviendas": forms.NumberInput(attrs={"class": "form-control"}),
            "numero_parques": forms.Select(attrs={"class": "form-select"}),
            "numero_edificios_residenciales": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "parroquia": forms.Select(attrs={"class": "form-select"}),
        }
