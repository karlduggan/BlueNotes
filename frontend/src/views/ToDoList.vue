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

<style lang="scss" scoped>
h3 {
  text-align: center;
  color: rgb(134, 134, 134)
}
.top {
  display: flex;
  justify-content: center;
}
.bottom {
  display: flex;
  justify-content: center;
}

</style>