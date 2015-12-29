# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u54c1\u7a2e')),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_date', models.DateField(default=datetime.date(2015, 12, 30), verbose_name='\u767b\u9332\u65e5')),
                ('comment', models.CharField(max_length=255, verbose_name='\u611f\u60f3', blank=True)),
                ('cultivar', models.ForeignKey(verbose_name='\u54c1\u7a2e', to='mysite.Cultivar', null=True)),
            ],
        ),
    ]
