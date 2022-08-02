<template>
  <div id="app" fluid>
    <!-- Nav Bar -->
    <NavBarComponent title="Vue and Django API Testing"/>
    <!-- Router Links -->
      <router-link to='/todo-list'>ToDo List</router-link>
      <!-- Router View -->
      <router-view></router-view>

  </div>
 
</template>

<script>
import NavBarComponent from './components/NavBarComponent.vue';
export default {
  components: {
    NavBarComponent
}
}
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
 
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
