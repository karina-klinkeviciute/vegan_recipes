from rest_framework import serializers

from recipe.models import Measurement, Product, Ingredient, Recipe


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer for Measurements
    """

    class Meta:
        model = Measurement
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for Ingredients
    """

    class Meta:
        model = Product
        fields = "__all__"


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe Ingredients
    """

    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for Recipe
    """

    class Meta:
        model = Recipe
        # fields = "__all__"
        fields = (
            "title",
            # "time_required",
            "difficulty",
            "description",
            "photo",
            "ingredients"
        )
        depth = 2
