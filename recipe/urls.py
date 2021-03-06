from django.conf.urls import url, include

from recipe.views import RecipeListView

urlpatterns = [
    url(r'^$', RecipeListView.as_view(template_name="recipe/home.html")),
    url(r'^recipes/$', RecipeListView.as_view(template_name="recipe/recipe_list.html")),
    url(r'api/', include('recipe.api.urls')),
]
