# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 02:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVICE', '0003_auto_20171210_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
