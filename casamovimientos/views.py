# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.views.generic import TemplateView
from userprofiles.mixins import LoginRequiredMixin
from django.db.models import Sum
from .models import CasaMovimiento


class ResumeView(LoginRequiredMixin, TemplateView):
    template_name = 'resume_view.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['resumen_cuentas'] = CasaMovimiento.objects.aggregate(
                total_monto_apartado=Sum('monto_apartado'),
                suma_aut=Sum('importe_tot_venta'),
                suma_tot=Sum('importe_tot_vendido'),
                suma_cobrado=Sum('importe_tot_cobrado'),
                suma_cobrar=Sum('importe_tot_cobrar'),
                suma_vender=Sum('importe_tot_vender'),
                suma_cret_puente=Sum('pago_adeu_cret_puente'),
                suma_comision=Sum('presupuesto_comision'),
                suma_pagar=Sum('faltante_x_pagar'))
        return context
