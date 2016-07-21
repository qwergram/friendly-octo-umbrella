# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('maximum_threads', models.IntegerField(default=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('password', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='head_of', to='boardapp.Post')),
                ('posts', models.ManyToManyField(related_name='thread', to='boardapp.Post')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='threads',
            field=models.ManyToManyField(related_name='board', to='boardapp.Thread'),
        ),
    ]
