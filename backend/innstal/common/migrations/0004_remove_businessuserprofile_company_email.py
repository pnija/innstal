# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_businessuserprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessuserprofile',
            name='company_email',
        ),
    ]