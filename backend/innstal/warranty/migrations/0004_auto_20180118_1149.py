# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0003_warranty_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='additional_info',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]