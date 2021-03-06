# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVICE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(help_text='johnorjane_doe@email.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(help_text='First Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(help_text='Last Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.CharField(help_text='Rating', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='review',
            field=models.CharField(help_text='Review', max_length=100),
        ),
    ]
