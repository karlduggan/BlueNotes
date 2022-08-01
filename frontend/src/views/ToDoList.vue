<template>
  <div class="app-container">
    <div class="top">
      <CreateTaskComponent/>
    </div>
    <div class="bottom">
      <ListTaskComponent/>
    </div>
  </div>
</template>

<script>


import CreateTaskComponent from '@/components/CreateTaskComponent.vue';
import ListTaskComponent from '@/components/ListTaskComponent.vue';

export default {
  name: 'ToDoList',
  components: {
    CreateTaskComponent,
    ListTaskComponent
}
}
</script>

<style>
h3 {
  text-align: center;
  color: rgb(134, 134, 134)
}
.app-container {

}
.top {
  display: flex;
  justify-content: center;
}
.bottom {
  display: flex;
  justify-content: center;
}
#app {
  
  font-family:  sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  
 

}
</style>