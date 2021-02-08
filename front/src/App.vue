<template>
  <div id="app">
    <header>Vegan Recipes</header>
    <div>
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
body {
  padding: 0;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #125701;
  margin: 0;
  padding: 0;
}

header {
color: #a9eb03;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 48px;
  margin-bottom: 50px;
}
</style>
