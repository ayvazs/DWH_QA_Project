# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=50)),
                ('connection_string', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=50)),
                ('data_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.DataBase')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=200)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.Schema')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_etalon', models.CharField(max_length=1000)),
                ('script_tested', models.CharField(max_length=1000)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.Table')),
            ],
        ),
    ]
