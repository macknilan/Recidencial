# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import Comprador


class CompradorCreateForm(ModelForm):
    class Meta:
        model = Comprador
        fields = ["nombre", "a_paterno", "a_materno"]
        # labels = { 'nombre': ('Nombre(s)'), }
        # help_texts = { 'nombre': ('Nombre(s) del comprador'), }
        widgets = {'nombre': forms.TextInput(attrs={'placeholder': 'Nombre(s)', 'title': 'Nombre del cliente'}),
                    'a_paterno': forms.TextInput(attrs={'placeholder': 'Apellido paterno', 'title': 'Apellido paterno'}),
                    'a_materno': forms.TextInput(attrs={'placeholder': 'Apellido materno', 'title': 'Apellido materno'}),
                    }
