<template >
  <div class="app-container" v-if="this.$store.state.isAuthenticated">
    <div class="wrapper">
        <div class="left">
          <div class="back-btn" @click="$router.push('/dashboard')">
            <p>Back</p>
          </div>
       
        <CreateTicketComponent/>
        </div>
        <div class="middle">
        <ListTaskComponent/>
    
        <!--<p>{{ $store.state.taskList }}</p>-->
        </div>

        <transition name="fade">
            <div v-if="this.$store.state.showComments" class="right">
                <div class="right-wrapper">
                    <CreateCommentComponent/>
             
                    <!--button @click="hideComments">Hide</button-->
                    <CommentListComponent/>
                </div>
                
            </div>
        </transition>
        
    </div>
   
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import CreateTicketComponent from '@/components/CreateTicketComponent.vue';
import ListTaskComponent from '@/components/ListTaskComponent.vue';
import CommentListComponent from '@/components/CommentListComponent.vue';
import CreateCommentComponent from '@/components/CreateCommentComponent.vue';


export default {
  name: 'ToDoList',
  components: {
    CreateTicketComponent,
    ListTaskComponent,
    CommentListComponent,
    CreateCommentComponent,
  
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
            // Get the Project id selected from the stoe state and append to the url
            const url = "http://127.0.0.1:8000/api/ticket-list-by-project-id/" + this.$store.state.selectedProjectID;
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Token ' + this.$store.state.token
            }}
            let response = await fetch(url, options);
            let data = await response.json()
            this.$store.state.ticketList = data;
          
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
  this.$store.state.selectedProjectID = localStorage.getItem('projectID')
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

   background-color: $background-color-3;
   // Off set the header with calc 
   min-height: calc(100vh - 68px);
   
}
.wrapper {
    display: flex;
    flex-direction: row;
    width: 100%;

}
.left {
  padding: 15px;
  background-color: $background-color-3;
  flex-grow: 1;
  max-width: 300px;

}
.middle {
position: relative;
border-left: solid 1px $border-color-1;
background-color: $background-color;
flex-grow: 2;
flex-basis: auto;
align-self: auto;
}
.right {
position: relative;
min-width: 300px;
border-left: solid 1px $border-color-1;
background-color: $background-color-3;
padding: 15px;
flex-grow: 1;
flex-basis: auto;
align-self: auto;
}
.right-wrapper{
    padding: 10px;
}
.back-btn {
  color: $border-color-2;
  margin-left: 10px;
  cursor: pointer;
  width: fit-content; 
}
.back-btn p {
  border-bottom: solid 1px $border-color-2;
  transition: all 200ms ease-in-out;
  font-weight: 500;
}
.back-btn p:hover {
  color: $white;
  border-bottom: 1px solid $white;
}
</style>