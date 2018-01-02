# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180102_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Package Name')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Package Title')),
                ('price', models.CharField(max_length=50, verbose_name='Package Cost')),
                ('duration', models.DurationField(blank=True, default=2000, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
