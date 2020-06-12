# Generated by Django 3.0.5 on 2020-05-02 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20170215_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('difficult', 'Master')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_required',
            field=models.IntegerField(blank=True, help_text='Enter total cooking time in minutes, approximately', null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(blank=True, help_text='Select an ingredient from the list or add a new one', null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='measurement',
            field=models.ForeignKey(blank=True, help_text='Select a type of measurement or add one (optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.Measurement'),
        ),
    ]
