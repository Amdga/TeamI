# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trimit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='userhairimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='PageImage',
        ),
        migrations.DeleteModel(
            name='UserHairImage',
        ),
    ]
