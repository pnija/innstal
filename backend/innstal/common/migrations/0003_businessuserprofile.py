# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 06:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_auto_20180111_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('0', 'Admin'), ('1', 'General'), ('2', 'Business')], default=1, max_length=1)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='mobile number')),
                ('person_to_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar_directory_path/')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
