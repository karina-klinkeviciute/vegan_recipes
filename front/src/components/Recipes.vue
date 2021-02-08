<template>
  <div id="recipes container" class="recipes">
<!--<div v-for="ingredient in allIngredients" :key="ingredient.id">{{ ingredient.product.name }}</div>-->
    <div v-for="recipe in allRecipes" :key="recipe.id" class="recipe">
      <div class="recipe-title">{{ recipe.title }}</div>
      <img alt="Illustration for the recipe" class="recipe-photo" src="../assets/beach-cocktail.jpg" />
      <span class="recipe-info">Time: {{recipe.timeRequired}} </span>
      <span class="recipe-difficulty">Difficulty: {{recipe.difficulty}}</span>
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
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  justify-content: space-evenly;
}
.recipe {
  background: rgba(256, 256, 256, 0.8);
  max-width: 300px;
  flex-basis: auto;
  color: #125701;
  margin: 5px;
  padding: 10px;
  border-radius: 5px;
  justify-content: flex-start;
  align-self: flex-start;
}

.recipe-photo {
  max-width: 300px;
  max-height: 300px;
}
</style>