# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
