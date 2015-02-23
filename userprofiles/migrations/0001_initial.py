# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import userprofiles.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'avatars', blank=True)),
                ('grupo', models.IntegerField(default=0, max_length=2, verbose_name=b'Grupo', choices=[(0, b'Sin grupo'), (1, b'Grupo uno'), (2, b'Grupo dos'), (3, b'Grupo tres')])),
                ('slug', models.CharField(max_length=100, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(userprofiles.models.SlugMixin, models.Model),
        ),
    ]
