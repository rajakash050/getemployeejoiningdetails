# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-05 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('member_desc', models.CharField(max_length=100)),
                ('memberid', models.IntegerField(max_length=11)),
            ],
        ),
    ]
