# -*- coding: utf-8 -*-


from django import forms
# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CasaGeneral


class CasaGeneralForm(ModelForm):
    class Meta:
        model = CasaGeneral
        fields = ['manzana', 'lote', 'etapa', 'status', ]
