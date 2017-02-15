from django.shortcuts import render
from django.views.generic import ListView
from recipe.models import Recipe
# Create your views here.

class RecipeListView(ListView):
    """
    A view for a recipe
    """
    model=Recipe
