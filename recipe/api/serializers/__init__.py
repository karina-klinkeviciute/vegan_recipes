from rest_framework import serializers

from recipe.models import Measurement, Ingredient, RecipeIngredient, Recipe


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer for Measurements
    """
    model = Measurement

    class Meta:
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for Ingredients
    """
    model = Ingredient

    class Meta:
        fields = "__all__"


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe Ingredients
    """
    model = RecipeIngredient

    class Meta:
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe
    """
    model = Recipe

    class Meta:
        fields = "__all__"
