<template>
  <div class="app-container">
    <div class="wrapper">
        <div class="left">
        <CreateTaskComponent/>
        </div>
        <div class="right">
        <ListTaskComponent/>
    
        <!--<p>{{ $store.state.taskList }}</p>-->
        </div>
        
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
},
data() {
  return {

  }
},  
methods: {
           fetchData: async function(){
            const url = "http://127.0.0.1:8000/api/task-list/";
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {'Content-Type': 'application/json'
            }}
            let response = await fetch(url, options);
            let data = await response.json()
            this.$store.state.taskList = data;
          
        }
},

beforeMount() {
  this.fetchData()
},
}
</script>

<style lang="scss" scoped>
h3 {
  text-align: center;
  color: rgb(134, 134, 134)
}
.app-container {
   display: flex;
   justify-content: center;
    background-color: $background-color-3;

   
}
.wrapper {
    display: flex;
}
.left {
  padding: 15px;
  background-color: $background-color-3;
}
.right {
position: relative;
right: 0;
border-left: solid 1px $border-color-1;
background-color: $background-color;

}

</style>