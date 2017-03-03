# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-19 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipeingredient_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(blank=True, help_text='Amount of an ingredient needed for recipe', null=True),
        ),
    ]