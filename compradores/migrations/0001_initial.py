# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, verbose_name=b'Nombre(s)')),
                ('a_paterno', models.CharField(max_length=140, verbose_name=b'Apellido paterno')),
                ('a_materno', models.CharField(max_length=140, verbose_name=b'Apellido materno')),
                ('userprofile', models.ForeignKey(to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
