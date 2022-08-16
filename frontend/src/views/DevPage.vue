<template >

  <div class="app-container" v-if="this.$store.state.isAuthenticated">
  
  <CreateTicket v-show="this.$store.state.showAddTicketModal"></CreateTicket>
    <div class="wrapper">
        
        
        <div class="middle">
         
          <div class="btn-wrapper">
               <button class="add-ticket-btn" @click="showCreateTicket">Add Ticket</button>
          </div>
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
import ListTaskComponent from '@/components/ListTaskComponent.vue';
import CommentListComponent from '@/components/CommentListComponent.vue';
import CreateCommentComponent from '@/components/CreateCommentComponent.vue';
import CreateTicket from '@/components/CreateTicket.vue';



export default {
  name: 'DevPage',
  components: {
   
    ListTaskComponent,
    CommentListComponent,
    CreateCommentComponent,
    CreateTicket
},
setup(){
    const showDrop = ref(true);
    const createTicketIsShow = ref(true);
        return {
            showDrop,
            createTicketIsShow
        }
},
data() {
  return {
     
  }
 
},  
methods: {
  showCreateTicket: function(){
    this.$store.state.showAddTicketModal = true;
  },
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
   height: 100%;
   
}
.wrapper {
    display: flex;
}
.left {
  padding: 15px;
  background-color: $background-color-3;
  min-width: 300px;
}
.middle {
position: relative;
border-left: solid 1px $border-color-1;
background-color: $background-color;
}
.right {
position: relative;
min-width: 300px;
border-left: solid 1px $border-color-1;
background-color: $background-color-3;
padding: 15px;
}
.right-wrapper{
    padding: 10px;
}
.btn-wrapper{
  padding: 25px;
  border-bottom: 4px solid $border-color-2;
  
}
.add-ticket-btn{
    width: 150px;
    padding: 15px;
   
    border: solid $green 1px;
    border-radius: 5px;
    background-color: $background-color-2;
    font-weight: 800;
    color: $green;
    cursor: pointer;
    transition: all 300ms ease;
}
.add-ticket-btn:hover {
 
  background-color: $green;
  color: $white;
}

</style>