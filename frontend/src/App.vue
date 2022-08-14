<template>
  <div id="app" fluid>
    <!-- Nav Bar -->
    <NavBarComponent class="navbar" username="Karl"/>
    
    <!-- Router Links -->
      <!--router-link to='/todo-list'>ToDo List</router-link-->
      <!--router-link to='/dev'>Dev Page</router-link-->
      <!-- Router View -->
      <router-view>
        
      </router-view>
    

  </div>
 
</template>

<script>

import NavBarComponent from './components/NavBarComponent.vue';

export default {
  components: {
    NavBarComponent,
  
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
  
   min-height: calc(100vh - 68px);
}
.navbar {
  position: relative;
}


</style>
