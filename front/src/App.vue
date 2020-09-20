<template>
  <div id="app">
    <img alt="Fruits background" src="./assets/fruits_bg.png" class ="background">

    <header>Vegan Recipes</header>

    <div class="recipes">
      <AllRecipes/>
    </div>

  </div>
</template>

<script>
import AllRecipes from "@/components/Recipes";

export default {
  name: 'App',
  components: {
    AllRecipes
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.background
{
  position: absolute;
  top: 0;
  left: 0;
  z-index: -999;
}
.recipes {
  background: rgba(256, 256, 256, 0.9);
  max-width: 500px;
}

header {

}
</style>
