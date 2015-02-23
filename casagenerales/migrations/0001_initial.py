# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manzana', models.IntegerField(default=0, max_length=2, verbose_name=b'Manzana', choices=[(0, b'Cero'), (1, b'Uno'), (2, b'Dos'), (3, b'Tres'), (4, b'Cuatro'), (5, b'Cinco'), (6, b'Seis'), (7, b'Siete'), (8, b'Ocho'), (9, b'Nueve'), (10, b'Diez')])),
                ('lote', models.IntegerField(default=0, max_length=1, verbose_name=b'Lote', choices=[(0, b'Cero'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'9'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20')])),
                ('etapa', models.CharField(default=b'selec_et', max_length=15, verbose_name=b'Etapa', choices=[(b'selec_et', b'Selecciona etapa'), (b'etapa_1_40', b'ETAPA 1 (40)')])),
                ('status', models.CharField(default=b'selec_sts', max_length=10, verbose_name=b'Status', choices=[(b'selec_sts', b'Selecciona status'), (b'apartada', b'Apartada'), (b'pagada', b'Pagada')])),
                ('comprador', models.OneToOneField(to='compradores.Comprador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
