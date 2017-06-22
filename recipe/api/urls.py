from rest_framework import routers

from recipe.api.views import RecipeAPIViewSet

router = routers.DefaultRouter()

router.register(r'recipes', RecipeAPIViewSet)

urlpatterns = router.urls
