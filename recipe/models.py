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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
          to=Ingredient,
          help_text=_("Select an ingredient from the list or add a new one"),
          on_delete=models.SET_NULL,
          null=True,
          blank=True
          )
    measurement = models.ForeignKey(
          to=Measurement,
          help_text=_("Select a type of measurement or add one (optional)"),
          null=True,
          blank=True,
          on_delete=models.SET_NULL
          )
    amount = models.FloatField(
          help_text="Amount of an ingredient needed for recipe",
          null=True,
          blank=True
          )

    def __str__(self):
        return "{}".format(self.ingredient.name)


class DifficultyChoices(object):
    EASY=1
    MEDIUM=2
    DIFFICULT=3
    CHOICES=(
         ("easy", _("Easy")),
          ("medium", _("Medium")),
          ("difficult", _("Master"))
          )


class Recipe(models.Model):
    title = models.TextField(help_text=_("Recipe title"))
    ingredients = models.ManyToManyField(
          to=RecipeIngredient,
          help_text=_("select or add an ingredient with measurement"))
    time_required = models.IntegerField(
          null=True,
          blank=True,
          help_text=_("Enter total cooking time in minutes, approximately"))
    difficulty = models.CharField(
          null=True,
          blank=True,
          max_length=255,
          choices=DifficultyChoices.CHOICES)
    description = models.TextField(
          help_text=_("Enter preparation and cooking instructions here")
          )
    photo = models.ImageField(
        null=True,
        blank=True
        )

    def __str__(self):
        return self.title
