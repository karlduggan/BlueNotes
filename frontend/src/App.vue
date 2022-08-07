<template>
  <div id="app" fluid>
    <!-- Nav Bar -->
    <NavBarComponent username="Karl"/>
    
    <!-- Router Links -->
      <!--router-link to='/todo-list'>ToDo List</router-link-->
      <!--router-link to='/dev'>Dev Page</router-link-->
      <!-- Router View -->
      <router-view ></router-view>
      <FooterComponent></FooterComponent>

  </div>
 
</template>

<script>

import NavBarComponent from './components/NavBarComponent.vue';
import FooterComponent from './components/FooterComponent.vue';
export default {
  components: {
    NavBarComponent,
    FooterComponent
},
/*
beforeCreate() {
  this.$store.commit('initializeStore')

  const token = this.$store.state.token
  if(token){
    axios.defaults.headers.common['Authorization'] = "Token " + token
  }  else {
    axios.defaults.header.common['Authorization'] = ''
  }
},
*/
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
  min-height: 100vh;


}



</style>
