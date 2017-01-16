from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Measurement(models.Model):
     """
     A class for measurements of ingredients
     """
     name = models.CharField(
          max_length=255, 
          help_text=_('A name of a measurement, for example "kilogram"')
          )
     abbreviation = models.CharField(
          max_length=20,
          help_text=_('An abreviation of a measurement, for example "kg"')
          )

class Ingredient(models.Model):
     """
     A class for ingredients
     """
     name = models.CharField(
          max_length=255,
          help_text=_("A name of an ingredient")
          )
     description = models.TextField(
          help_text=_("A description (optional)"),
          null=True,
          blank=True
          )
          
class Recipe(models.Model)
     title = models.TextField(help_text=_("Recipe title")
     