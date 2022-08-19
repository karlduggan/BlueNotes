<template >

  <div class="app-container" v-if="this.$store.state.isAuthenticated">
  
  <CreateTicket v-show="this.$store.state.showAddTicketModal"></CreateTicket>
    <div class="wrapper">
        
        
        <div class="middle-wrapper">
            <div class="btn-wrapper">
              <div class="items-inline">
                <h1>Project Name </h1>
              </div>
              
               <button id="add-ticket-btn" class="items-inline" @click="showCreateTicket">Add Ticket</button>
                <button id="assigned-btn" class="items-inline">Assigned</button>
                <button id="export-btn" class="items-inline">Export</button>

                <select name="sortBy" id="sort-select" class="items-inline">
                    <option value="" disabled selected>Sort By</option>
                    <option value="Priority">Priority</option>
                    <option value="CreatedBy">Created By</option>
                    <option value="DueSoon">Due Soon</option>
                    <optgroup label="Sort by Status">
                        <option value="InProgress">In Progress</option>
                        <option value="To Do">To Do</option>
                        <option value="Completed">Completed</option>
                        <option value="OverDue">Over Due</option>
                    </optgroup>
                </select>
            </div>
            <div class="middle">
              <ListTaskComponent/>
            </div>
         
        
    
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
   background-color: $background-color;
   // Off set the header with calc 
   min-height: calc(100vh - 68px);
   
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
/*
border-left: solid 1px $border-color-1;
border-right: solid 1px $border-color-1;

background-color: $background-color;

*/
}
.right {
position: relative;
min-width: 300px;

background-color: $background-color-3;
padding: 15px;
}
.right-wrapper{
    padding: 10px;
}
.btn-wrapper{
  padding: 20px 0px 20px 0px;
  border-bottom: 4px solid $border-color-2;
  display: flex;

  
}
#add-ticket-btn{
    width: 125px;
    padding: 10px;
   
    border: solid $green 1px;
    border-radius: 5px;
    background-color: transparent;
    font-weight: 800;
    color: $green;
    cursor: pointer;
    transition: all 300ms ease;
}
#add-ticket-btn:hover {
 
  background-color: $green;
  color: $white;
}

#assigned-btn {
    width: 125px;
    padding: 10px;
    border: solid $blue 1px;
    border-radius: 5px;
    background-color: transparent;
    font-weight: 800;
    color: $blue;
    cursor: pointer;
    transition: all 300ms ease;
}
#assigned-btn:hover {
    background-color: $blue;
    color: $white;
}



#export-btn {
    width: 125px;
    padding: 10px;
   
    border: solid $pink 1px;
    border-radius: 5px;
    background-color: transparent;
    font-weight: 800;
    color: $pink;
    cursor: pointer;
    transition: all 300ms ease;
}
#export-btn:hover {
    background-color: $pink;
    color: $white;
}

#sort-select {
    float: right;
    width: 125px;
    padding: 10px;
    text-align: center;
    border: solid $orange 1px;
    border-radius: 5px;
    background-color: transparent;
    font-weight: 800;
    color: $orange;
    cursor: pointer;
    transition: all 300ms ease;
    outline: none;
    justify-content: flex-end;
    -webkit-appearance:none;
}
#sort-select:hover {
    background-color: $orange;
    color: $white;
}
#sort-select:focus {
    outline: 0;
}
.items-inline {
    margin-right: 20px;
   
}
.items-inline h1 {
  padding: 0;
  margin: 0;
  color: $border-color-2;
  font-size: 25px;
  position: relative;
  top: 5px;
}
</style>