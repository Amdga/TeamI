# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-01 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trimit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='picture',
            field=models.ImageField(blank=True, upload_to='review_images'),
        ),
    ]
