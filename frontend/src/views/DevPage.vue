<template >
  <div class="app-container" v-if="this.$store.state.isAuthenticated">
    <div class="wrapper">
        <div class="left">
        <CreateTaskComponent/>
        </div>
        <div class="middle">
        <ListTaskComponent/>
    
        <!--<p>{{ $store.state.taskList }}</p>-->
        </div>
        <transition name="fade">
            <div v-if="this.$store.state.showComments" class="right">
                <h1>comments</h1>
                <button @click="hideComments">Hide</button>
                <CommentListComponent/>
            </div>
        </transition>
        
    </div>
   
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import CreateTaskComponent from '@/components/CreateTaskComponent.vue';
import ListTaskComponent from '@/components/ListTaskComponent.vue';
import CommentListComponent from '@/components/CommentListComponent.vue';

export default {
  name: 'DevPage',
  components: {
    CreateTaskComponent,
    ListTaskComponent,
    CommentListComponent
},
setup(){
    const showDrop = ref(true);
        return {
            showDrop
        }
},
data() {
  return {

  }
 
},  
methods: {
           fetchData: async function(){
            const url = "http://127.0.0.1:8000/api/ticket-list/";
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Token ' + this.$store.state.token
            }}
            let response = await fetch(url, options);
            let data = await response.json()
            this.$store.state.taskList = data;
          
        },
        hideComments: function(){
            this.$store.state.showComments = false;
        }
},
beforeCreate() {
  this.$store.commit('initializeStore')

  const token = this.$store.state.token
  if(token){
    axios.defaults.headers.common['Authorization'] = "Token " + token
  }  else {
    axios.defaults.headers.common['Authorization'] = ''
  }
},

beforeMount() {
  this.fetchData()
},
created(){
  // Work around to have a persistent data and to not loose the username when refreshing the page 
  this.$store.state.username = localStorage.getItem('username')
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
   min-height: 90vh;
   
}
.wrapper {
    display: flex;
    
}
.left {
  padding: 15px;
  background-color: $background-color-3;
  min-width: 400px;
}
.middle {
position: relative;
border-left: solid 1px $border-color-1;
background-color: $background-color;
}
.right {
position: relative;
min-width: 400px;
border-left: solid 1px $border-color-1;
background-color: $background-color-3;
}

</style>