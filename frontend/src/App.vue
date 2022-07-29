<template>
  <div>
    <p>Testing Django API</p>
    <EntryComponent id=1 title="Testing Title" content="this is a test to find out what works"/>
  </div>
</template>

<script>
import EntryComponent from './components/EntryComponent.vue';




export default {
  name: 'App',
  components: {
    EntryComponent
}
}
</script>

<style>
* {
padding: 0;
margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  
 

}
</style>
