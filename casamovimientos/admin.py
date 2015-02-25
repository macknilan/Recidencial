# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import CasaMovimiento
from actions import export_as_excel

class CasaMovimientoAdmin(admin.ModelAdmin):
    list_display = ('comprador', 'monto_credito', 'fecha_de_apartado', 'monto_apartado', 'enganche', 'infonavit_foviste', 'banco', 'fecha_programada_firma', 'fecha_de_firma', 'dias_transcurridos', 'dias_de_retraso', 'importe_tot_venta', 'diferencia_a_pagar', 'importe_tot_vendido', 'otros_ingresos_venta', 'importe_tot_cobrado', 'importe_tot_cobrar', 'importe_tot_vender', 'pago_adeu_cret_puente', 'base_cret_puente', 'tipo_credito', 'presupuesto_comision', 'pagado_acum_comi', 'faltante_x_pagar', 'comi_ecu', )
    list_filter = ('comprador', )
    search_fields = ('comprador__nombre', 'comprador__a_paterno', 'comprador__a_materno', )
    actions = (export_as_excel, )

admin.site.register(CasaMovimiento, CasaMovimientoAdmin)
