<template>
  <div>
<div v-for="ingredient in allIngredients" :key="ingredient.id">{{ ingredient.product.name }}</div>
</div></template>

<script>
import gql from 'graphql-tag';
export default {
name: "allIngredients",
  apollo: {
    allIngredients: gql`
    query{
      allIngredients {
        id
        product {
          name }
        }
        }
    `
  }
}
</script>

<style scoped>

</style>