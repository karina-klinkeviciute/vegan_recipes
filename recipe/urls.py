from django.conf.urls import url, include
from django.contrib import admin
from recipe.views import RecipeListView

urlpatterns = [
    url(r'^$', RecipeListView.as_view(template_name="recipe/home.html")),
    url(r'^recipes/$', RecipeListView.as_view(template_name="recipe/recipe_list.html")),
]
