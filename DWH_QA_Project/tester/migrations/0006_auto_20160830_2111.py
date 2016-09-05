# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0005_auto_20160826_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='test_value_completeness_source',
            new_name='test_value_completeness_source_dev',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='test_value_completeness_target',
            new_name='test_value_completeness_target_dev',
        ),
        migrations.AddField(
            model_name='table',
            name='test_value_completeness_source_prod',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='test_value_completeness_target_prod',
            field=models.BigIntegerField(null=True),
        ),
    ]