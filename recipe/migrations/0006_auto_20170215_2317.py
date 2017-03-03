# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20170119_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('difficult', 'Master')], max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_required',
            field=models.IntegerField(help_text='Enter total cooking time in minutes, approximately'),
        ),
    ]