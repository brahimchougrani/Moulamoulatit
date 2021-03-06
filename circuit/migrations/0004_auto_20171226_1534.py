# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuit', '0003_homedetail_histoire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetail',
            name='description1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='description3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='histoire',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='img_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='homedetail',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
