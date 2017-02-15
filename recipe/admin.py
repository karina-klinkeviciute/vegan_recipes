from django.contrib import admin
from recipe.models import Ingredient, RecipeIngredient, Recipe, Measurement

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Recipe)
admin.site.register(Measurement)