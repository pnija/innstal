# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0005_businessuserprofile_is_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.PricingPlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]