# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-16 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20180116_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Country'),
        ),
    ]
