# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11 on 2018-01-09 08:32
=======
# Generated by Django 1.11 on 2018-01-10 08:13
>>>>>>> feature/warranty
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('common', '0003_pricingplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_color', models.CharField(blank=True, max_length=200, null=True)),
                ('product_serial_no', models.CharField(blank=True, max_length=30, null=True)),
                ('purchase_country', models.CharField(blank=True, max_length=200, null=True)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('additional_info', models.CharField(blank=True, max_length=200, null=True)),
                ('warranty_image', models.ImageField(upload_to='warranty_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductType')),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.UserProfile')),
            ],
        ),
    ]
