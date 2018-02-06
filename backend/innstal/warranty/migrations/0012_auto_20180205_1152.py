# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0011_auto_20180205_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimedwarranty',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_claimed_warranty', to='common.UserProfile'),
        ),
        migrations.AlterField(
            model_name='claimedwarranty',
            name='warranty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warranty.Warranty'),
        ),
    ]
