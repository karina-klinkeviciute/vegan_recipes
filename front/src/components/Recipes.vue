<template>
  <div id="recipes">
<!--<div v-for="ingredient in allIngredients" :key="ingredient.id">{{ ingredient.product.name }}</div>-->
    <div v-for="recipe in allRecipes" :key="recipe.id" class="recipe">
      <div class="recipe-title">{{ recipe.title }}</div>
      <img alt="Illustration for the recipe" class="recipe-photo" src="../assets/beach-cocktail.jpg" />
      <div class="recipe-info">Time: {{recipe.timeRequired}}</div>
      <div class="recipe-difficulty">Difficulty: {{recipe.difficulty}}</div>
    </div>
  </div></template>

<script>
import gql from 'graphql-tag';
export default {
name: "allRecipes",
  apollo: {
    allRecipes: gql`
    query{
      allRecipes{
        id
         title
         timeRequired
         photo
         difficulty
  }
        }
    `
  }
}
</script>

<style scoped>
.recipes {
  display: flex;
}
.recipe {
  display: flex;
  background: rgba(256, 256, 256, 0.9);
  max-width: 400px;
}

.recipe-photo {
  max-width: 300px;
  max-height: 300px;
}
</style>