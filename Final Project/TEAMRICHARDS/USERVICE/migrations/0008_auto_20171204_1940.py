# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVICE', '0007_auto_20171204_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitycomment',
            name='author',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='carpoolcomment',
            name='author',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='textbookcomment',
            name='author',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tutorcomment',
            name='author',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]