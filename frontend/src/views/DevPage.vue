<template>
    <div>
        <h1>Welcome to the Dev Page</h1>
        <p>{{ $store.state.name}}</p>
        <p>{{ $store.state.taskList }}</p>
      <button @click="testState">Click Test</button>
      <button @click="fetchData">Click fecth data</button>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<img src="@/assets/comment_icon.svg" alt="" srcset="">
<CommentButton stroke-color="#0077B0" background-color="#0077B0"></CommentButton>
    </div>

</template>

<script>
import CommentButton from '../components/CommentButton.vue'



export default {
    setup() {
        return {
            
        }
    },
    
    components: {
    CommentButton
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