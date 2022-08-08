<template>
    <div>
        <h1>Welcome to the Dev Page</h1>
        <p>{{ $store.state.name}}</p>
        <p>{{ $store.state.taskList }}</p>
      <button @click="testState">Click Test</button>
      <button @click="fetchData">Click fecth data</button>

      <LoginForm></LoginForm>
    </div>

</template>

<script>
import LoginForm from '@/components/LoginForm.vue'



export default {
    setup() {
        return {
            
        }
    },
    
    components: {
    LoginForm
},
    name: 'DevPage',
    data() {
        return {
       
        }
    },



}

</script>

<style lang="scss" scoped>

</style>