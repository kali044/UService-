# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVICE', '0002_auto_20171028_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='review',
            field=models.CharField(help_text='Review', max_length=500),
        ),
    ]
