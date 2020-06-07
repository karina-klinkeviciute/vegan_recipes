from rest_framework import viewsets, permissions

from recipe.api.serializers import MeasurementSerializer, IngredientSerializer, RecipeIngredientSerializer, \
    RecipeSerializer
from recipe.models import Measurement, Product, Ingredient, Recipe


class MeasurementAPIViewSet(viewsets.ModelViewSet):
    """
    Viewset for Measurements
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class IngredientAPIViewSet(viewsets.ModelViewSet):
    """
    Viewset for Measurements
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = IngredientSerializer


class RecipeIngredientAPIViewSet(viewsets.ModelViewSet):
    """
    Viewset for Measurements
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Ingredient.objects.all()
    serializer_class = RecipeIngredientSerializer


class RecipeAPIViewSet(viewsets.ModelViewSet):
    """
    Viewset for Measurements
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
