# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-16 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleSpider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ips',
            name='ip_port',
        ),
    ]
