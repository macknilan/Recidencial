# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casamovimientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casamovimiento',
            name='banco',
            field=models.DecimalField(verbose_name=b'Banco', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='base_cret_puente',
            field=models.DecimalField(verbose_name=b'Base credito puente', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='comi_ecu',
            field=models.DecimalField(verbose_name=b'Comisi\xc3\xb2n jchavez', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='diferencia_a_pagar',
            field=models.DecimalField(verbose_name=b'Diferencia a pagar', editable=False, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='enganche',
            field=models.DecimalField(verbose_name=b'Enganche', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='faltante_x_pagar',
            field=models.DecimalField(verbose_name=b'Faltante por pagar', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='importe_tot_cobrado',
            field=models.DecimalField(verbose_name=b'Importe TOT cobrado', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='importe_tot_cobrar',
            field=models.DecimalField(verbose_name=b'Importe TOT por cobrar', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='importe_tot_vender',
            field=models.DecimalField(verbose_name=b'Total por vender', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='importe_tot_vendido',
            field=models.DecimalField(verbose_name=b'Importe TOT vendido', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='importe_tot_venta',
            field=models.DecimalField(verbose_name=b'Importe total de venta (AUT)', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='infonavit_foviste',
            field=models.DecimalField(verbose_name=b'Infonavit / Fovissste', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='monto_apartado',
            field=models.DecimalField(verbose_name=b'Monto de apartado', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='monto_credito',
            field=models.DecimalField(verbose_name=b'Mondo de Cr\xc3\xa8dito', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='otros_ingresos_venta',
            field=models.DecimalField(verbose_name=b'Otros ingresos por venta', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='pagado_acum_comi',
            field=models.DecimalField(verbose_name=b'Pago acumulado comisi\xc3\xb2n', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='pago_adeu_cret_puente',
            field=models.DecimalField(verbose_name=b'Pago adeudo cr\xc3\xa8dito puente', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casamovimiento',
            name='presupuesto_comision',
            field=models.DecimalField(verbose_name=b'Presupuesto comisi\xc3\xb2n', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
