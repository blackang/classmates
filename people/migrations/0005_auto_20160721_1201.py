# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160721_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='myclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='people.MyClass', verbose_name='所属班级'),
        ),
    ]
