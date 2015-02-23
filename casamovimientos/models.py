# -*- coding: utf-8 -*-


from django.db import models
from compradores.models import Comprador
from datetime import date, timedelta
from decimal import Decimal


class CasaMovimiento(models.Model):
    NOM_CREDITO = (
        ('ninguno', 'Ninguno'),
        ('info_tradic', 'Info Tradic'),
        ('info_cony', 'Info Cony'),
        ('bancario', 'Bancario'),
        ('alia2_cony', 'Alia2 Cony'),
        ('info_tot', 'Info tot'),
        ('info_total_ag', 'Info Total AG'),
        ('cofi', 'Cofi'),
        ('tradicional', 'Tradicional'),
        ('fovissste', 'Fovissste'),
    )
    monto_credito = models.DecimalField("Mondo de Crèdito", max_digits=10, decimal_places=2)
    fecha_de_apartado = models.DateField("Fecha de apartado", auto_now=False, auto_now_add=False,)
    monto_apartado = models.DecimalField("Monto de apartado", max_digits=10, decimal_places=2)
    enganche = models.DecimalField("Enganche", max_digits=10, decimal_places=2)
    infonavit_foviste = models.DecimalField("Infonavit / Fovissste", max_digits=10, decimal_places=2)
    banco = models.DecimalField("Banco", max_digits=10, decimal_places=2)
    fecha_programada_firma = models.DateField("Fecha programada de firma", editable=False, blank=True)
    fecha_de_firma = models.DateField("Fecha de firma", auto_now=False, auto_now_add=False,)
    dias_transcurridos = models.IntegerField("Dìas transcurridos", editable=False, blank=True)
    dias_de_retraso = models.IntegerField("Dìas de retraso", editable=False, blank=True)
    importe_tot_venta = models.DecimalField("Importe total de venta (AUT)", max_digits=10, decimal_places=2)
    diferencia_a_pagar = models.DecimalField("Diferencia a pagar", max_digits=10, decimal_places=2, blank=True, editable=False)
    importe_tot_vendido = models.DecimalField("Importe TOT vendido", max_digits=10, decimal_places=2, editable=False)
    otros_ingresos_venta = models.DecimalField("Otros ingresos por venta", max_digits=10, decimal_places=2)
    importe_tot_cobrado = models.DecimalField("Importe TOT cobrado", max_digits=10, decimal_places=2, editable=False)
    importe_tot_cobrar = models.DecimalField("Importe TOT por cobrar", max_digits=10, decimal_places=2, editable=False)
    importe_tot_vender = models.DecimalField("Total por vender", max_digits=10, decimal_places=2, editable=False)
    pago_adeu_cret_puente = models.DecimalField("Pago adeudo crèdito puente", max_digits=10, decimal_places=2)
    base_cret_puente = models.DecimalField("Base credito puente", max_digits=10, decimal_places=2)
    tipo_credito = models.CharField("Tipo de crèdito", max_length=13, choices=NOM_CREDITO, default='ninguno')
    presupuesto_comision = models.DecimalField("Presupuesto comisiòn", max_digits=10, decimal_places=2, editable=False)
    pagado_acum_comi = models.DecimalField("Pago acumulado comisiòn", max_digits=10, decimal_places=2)
    faltante_x_pagar = models.DecimalField("Faltante por pagar", max_digits=10, decimal_places=2, editable=False)
    comi_ecu = models.DecimalField("Comisiòn jchavez", max_digits=10, decimal_places=2, editable=False)
    comprador = models.OneToOneField(Comprador)

    def save(self):
        self.fecha_programada_firma = self.fecha_de_apartado + timedelta(days=60)
        dif_dias = self.fecha_de_firma - self.fecha_de_apartado
        self.dias_transcurridos = dif_dias.days

        dif_retra = self.fecha_de_firma - self.fecha_programada_firma
        self.dias_de_retraso = dif_retra.days

        self.diferencia_a_pagar = (self.importe_tot_venta - self.monto_credito) + 10000
        self.importe_tot_vendido = self.importe_tot_venta
        self.importe_tot_cobrado = self.monto_apartado + self.enganche + self.infonavit_foviste + self.banco
        self.importe_tot_cobrar = (self.importe_tot_venta - self.importe_tot_cobrado) + self.otros_ingresos_venta

        if self.importe_tot_vendido > 0:
            self.importe_tot_vender = 0
        else:
            self.importe_tot_vender = self.importe_tot_venta

        self.presupuesto_comision = (self.importe_tot_venta * Decimal(1.5) / 100)
        self.faltante_x_pagar = self.presupuesto_comision - self.pagado_acum_comi
        self.comi_ecu = (self.importe_tot_venta * Decimal(0.33) / 100)

        super(CasaMovimiento, self).save()

    def __unicode__(self):
        return str(self.monto_credito)

#        return str("%.2f - %s - %.2f - %.2f - %.2f - %.2f - %s - %s - %d - %d - %.2f - \
#                %.2f - %.2f - %.2f - %.2f - %.2f - %.2f - %.2f - %s - %.2f - %.2f - \
#                %.2f - %.2f" % (
#                                        self.monto_credito,
#                                        self.fecha_de_apartado,
#                                        self.monto_apartado,
#                                        self.enganche,
#                                        self.infonavit_foviste,
#                                        self.banco,
#                                        self.fecha_programada_firma,
#                                        self.fecha_de_firma,
#                                        self.dias_transcurridos,
#                                        self.dias_de_retraso,
#                                        self.diferencia_a_pagar,
#                                        self.importe_tot_venta,
#                                        self.importe_tot_vendido,
#                                        self.importe_tot_cobrado,
#                                        self.importe_tot_cobrar,
#                                        self.importe_tot_vender,
#                                        self.pago_adeu_cret_puente,
#                                        self.base_cret_puente,
#                                        self.tipo_credito,
#                                        self.presupuesto_comision,
#                                        self.pagado_acum_comi,
#                                        self.faltante_x_pagar,
#                                        self.comi_ecu,
#                                    ))
