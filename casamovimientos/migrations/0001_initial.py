# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasaMovimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_credito', models.DecimalField(verbose_name=b'Mondo de Cr\xc3\xa8dito', max_digits=8, decimal_places=2)),
                ('fecha_de_apartado', models.DateField(verbose_name=b'Fecha de apartado')),
                ('monto_apartado', models.DecimalField(verbose_name=b'Monto de apartado', max_digits=8, decimal_places=2)),
                ('enganche', models.DecimalField(verbose_name=b'Enganche', max_digits=8, decimal_places=2)),
                ('infonavit_foviste', models.DecimalField(verbose_name=b'Infonavit / Fovissste', max_digits=8, decimal_places=2)),
                ('banco', models.DecimalField(verbose_name=b'Banco', max_digits=8, decimal_places=2)),
                ('fecha_programada_firma', models.DateField(verbose_name=b'Fecha programada de firma', editable=False, blank=True)),
                ('fecha_de_firma', models.DateField(verbose_name=b'Fecha de firma')),
                ('dias_transcurridos', models.IntegerField(verbose_name=b'D\xc3\xacas transcurridos', editable=False, blank=True)),
                ('dias_de_retraso', models.IntegerField(verbose_name=b'D\xc3\xacas de retraso', editable=False, blank=True)),
                ('importe_tot_venta', models.DecimalField(verbose_name=b'Importe total de venta (AUT)', max_digits=8, decimal_places=2)),
                ('diferencia_a_pagar', models.DecimalField(verbose_name=b'Diferencia a pagar', editable=False, max_digits=8, decimal_places=2, blank=True)),
                ('importe_tot_vendido', models.DecimalField(verbose_name=b'Importe TOT vendido', editable=False, max_digits=8, decimal_places=2)),
                ('otros_ingresos_venta', models.DecimalField(verbose_name=b'Otros ingresos por venta', max_digits=8, decimal_places=2)),
                ('importe_tot_cobrado', models.DecimalField(verbose_name=b'Importe TOT cobrado', editable=False, max_digits=8, decimal_places=2)),
                ('importe_tot_cobrar', models.DecimalField(verbose_name=b'Importe TOT por cobrar', editable=False, max_digits=8, decimal_places=2)),
                ('importe_tot_vender', models.DecimalField(verbose_name=b'Total por vender', editable=False, max_digits=8, decimal_places=2)),
                ('pago_adeu_cret_puente', models.DecimalField(verbose_name=b'Pago adeudo cr\xc3\xa8dito puente', max_digits=8, decimal_places=2)),
                ('base_cret_puente', models.DecimalField(verbose_name=b'Base credito puente', max_digits=8, decimal_places=2)),
                ('tipo_credito', models.CharField(default=b'ninguno', max_length=13, verbose_name=b'Tipo de cr\xc3\xa8dito', choices=[(b'ninguno', b'Ninguno'), (b'info_tradic', b'Info Tradic'), (b'info_cony', b'Info Cony'), (b'bancario', b'Bancario'), (b'alia2_cony', b'Alia2 Cony'), (b'info_tot', b'Info tot'), (b'info_total_ag', b'Info Total AG'), (b'cofi', b'Cofi'), (b'tradicional', b'Tradicional'), (b'fovissste', b'Fovissste')])),
                ('presupuesto_comision', models.DecimalField(verbose_name=b'Presupuesto comisi\xc3\xb2n', editable=False, max_digits=8, decimal_places=2)),
                ('pagado_acum_comi', models.DecimalField(verbose_name=b'Pago acumulado comisi\xc3\xb2n', max_digits=8, decimal_places=2)),
                ('faltante_x_pagar', models.DecimalField(verbose_name=b'Faltante por pagar', editable=False, max_digits=8, decimal_places=2)),
                ('comi_ecu', models.DecimalField(verbose_name=b'Comisi\xc3\xb2n jchavez', editable=False, max_digits=8, decimal_places=2)),
                ('comprador', models.OneToOneField(to='compradores.Comprador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
