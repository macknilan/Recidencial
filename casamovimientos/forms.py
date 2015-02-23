# -*- coding: utf-8 -*-


from django import forms
# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CasaMovimiento


class CasaMovimientoForm(ModelForm):

    class Meta:
        model = CasaMovimiento
        fields = ['monto_credito', 'fecha_de_apartado', 'monto_apartado', 'enganche', 'infonavit_foviste',
                  'banco', 'fecha_de_firma', 'importe_tot_venta', 'otros_ingresos_venta', 'pago_adeu_cret_puente',
                  'base_cret_puente', 'tipo_credito', 'pagado_acum_comi', ]
        widgets = {
            'monto_credito': forms.TextInput(attrs={'title': 'Monto de Crédito', 'placeholder': '123456789.99'}),
            'fecha_de_apartado': forms.DateInput(format=('%d/%m/%Y'), attrs={'title': 'MM/DD/YYYY - Formato de fecha', 'type': 'date'}),
            'monto_apartado': forms.TextInput(attrs={'title': 'Monto de Apartado', 'placeholder': '123456789.99'}),
            'enganche': forms.TextInput(attrs={'title': 'Enganche', 'placeholder': '123456789.99'}),
            'infonavit_foviste': forms.TextInput(attrs={'title': 'Infonavit/ Fovissste', 'placeholder': '123456789.99'}),
            'banco': forms.TextInput(attrs={'title': 'Banco', 'placeholder': '123456789.99'}),
            'fecha_de_firma': forms.DateInput(format=('%d/%m/%Y'), attrs={'title': 'MM/DD/YYYY - Formato de fecha', 'type': 'date'}),
            'importe_tot_venta': forms.TextInput(attrs={'title': 'Importe Total de Venta (AUT)', 'placeholder': '123456789.99'}),
            'otros_ingresos_venta': forms.TextInput(attrs={'title': 'Otros Ingresos por venta', 'placeholder': '123456789.99'}),
            'pago_adeu_cret_puente': forms.TextInput(attrs={'title': 'PAGO Adeudo Credito Puente', 'placeholder': '123456789.99'}),
            'base_cret_puente': forms.TextInput(attrs={'title': 'BASE CREDITO PUENTE', 'placeholder': '123456789.99'}),
            'tipo_credito': forms.Select(attrs={'title': 'Tipo de Credito', 'placeholder': '123456789.99'}),
            'pagado_acum_comi': forms.TextInput(attrs={'title': 'Pagado Acum Comision', 'placeholder': '123456789.99'}),
        }
