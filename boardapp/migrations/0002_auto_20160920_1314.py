# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='threads',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boardapp.Thread'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='boardapp.Board'),
            preserve_default=False,
        ),
    ]
