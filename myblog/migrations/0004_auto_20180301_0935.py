# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-01 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='链接名称')),
                ('url', models.CharField(max_length=100, verbose_name='链接')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]
