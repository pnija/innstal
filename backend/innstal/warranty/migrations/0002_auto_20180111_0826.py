# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='company_name',
            field=models.CharField(choices=[('--', '--'), ('LG', 'LG'), ('APPLE', 'APPLE'), ('Samsung', 'Samsung'), ('HTC', 'HTC')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='warranty',
            name='purchase_country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
