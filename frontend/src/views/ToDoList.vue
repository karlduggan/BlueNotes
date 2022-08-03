<template>
  <div class="app-container">
    <div class="wrapper">
        <div class="left">
        <CreateTaskComponent/>
        </div>
        <div class="right">
        <ListTaskComponent/>
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
}
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
   
}
.wrapper {
    display: flex;
}
.left {
  border: 2px solid $light-grey;
}
.right {
position: relative;
right: 0;
border: 2px solid $light-grey;

}

</style>