from django.contrib import admin
from recipe.models import Product, Ingredient, Recipe, Measurement

# Register your models here.

admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Measurement)