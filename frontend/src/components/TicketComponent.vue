<template>
    <div class="entry-container"  >

        <div class="entry-wrapper">

                <!-- Header Row STARTS-->
                <div class="header-row">
                    <div id="title"><p>{{title}}</p></div>

                    <!-- Priority STARTS -->
                    <div class="priority">
                        <p>{{priority}}</p>
                    </div>
                    <!-- Priority ENDS -->

                    <div class="countdown-container">
                        <!--Temp -->
                        <CountDownComponent :complete_date="dateToComplete" />
                    </div>
                

                    <div class="space">

                    </div>

                    <div class="status-container">
                        <DynamicStatusButtom :entryId="id" :status="status"/>
                    </div>
                </div>
                <!-- Header Row ENDS -->

                
                <!-- Dropdown Container BEGINS -->
                <transition name="fade">
                    <div v-if="showDrop" class="dropdown-container">
                        
                        <div class="time-stamp">
                        
                            <p>{{timestamp}}</p>
                            <p>Created By: <b>{{createdBy}}</b></p>
                        
                            <div class="button-container">
                                <div class="button" @click="openComments">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M7 7h10v2H7zm0 4h7v2H7z"  fill="#9AA4B8"/><path d="M20 2H4c-1.103 0-2 .897-2 2v18l5.333-4H20c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm0 14H6.667L4 18V4h16v12z" fill="#9AA4B8" /></svg>
                                </div>
                                <div class="button" @click="deleteEntry()">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z" fill="#9AA4B8" /><path d="M9 10h2v8H9zm4 0h2v8h-2z" fill="#9AA4B8"/></svg>
                                </div>
                            </div>
                        </div>
                        <div class="content-container">
                            <p>{{content}}</p>
                            <!--Testing Comment Button-->

         
                        </div>
                    </div>
                </transition>
                <!-- Dropdown Container ENDS -->
                
            </div>    
                
                
                <!--button @click="getID()">Get ID</button-->
                <div class="footer" @click="detailDropdown()">
                    <p>{{dropdownText}}</p>
                </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import DynamicStatusButtom from './DynamicStatusButtom.vue'
import CountDownComponent from './CountDownComponent.vue';


export default {
    setup(){
        const showDrop = ref(false);
        return {
            showDrop
        }
    },
    data(){
        return {
            newStatus: "",
            dropdownText: "View Details"
        }
    },
    name: "TicketComponent",
    props: [
        'index', 
        'id',
        'title',
        'content',
        'status', 
        'timestamp',
        'dateToComplete',
        'priority',
        'createdBy'
    ],
    components: {
    DynamicStatusButtom,
    CountDownComponent
},

    methods: {
        detailDropdown: function(){
            this.showDrop = !this.showDrop
            if(this.showDrop){
                this.dropdownText = "Hide Details"
            } else {
                this.dropdownText = "View Details"
            }
        },
        deleteEntry: function(){
            let confirmation = confirm("Are you sure you want to delete ticket?")
            if(confirmation == true){
                const url = "http://127.0.0.1:8000/api/ticket-delete/" + this.id;
                const options =  {
                method: 'DELETE',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + this.$store.state.token
                }}
                fetch(url, options)
                .then(response => response.json())
                .then(data =>  console.log(data))
                .catch( error => console.log(error.message))
                // Splice used to delete a specific item by index 
                this.$store.state.ticketList.splice(this.index, 1)
            }
        },
        test:function(){
            console.log("comment test click")
        },
        getCommentsFromTicketID: async function(ticketID){
            const url = "http://127.0.0.1:8000/api/comment-list/" + ticketID;
            const options = {
                method: "GET",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Token " + this.$store.state.token
                }
            };
            let response = await fetch(url, options);
            let data = await response.json();
            console.log(data)
            this.$store.state.commentList = data;
        },

        openComments:function(){
            console.log("comment btn test")
            // Check if showComments is True
            if (this.$store.state.showComments){
                // Set id to selectedTicketID
                this.$store.state.selectedTicketID = this.id;
                // Fetch api comment call
                this.getCommentsFromTicketID(this.id)
            }
            else{
                // Set showComment to True so to open comment section
                this.$store.state.showComments = true;
                // Set id to selectedTicketID
                this.$store.state.selectedTicketID = this.id;
                 // Fetch api comment call
                this.getCommentsFromTicketID(this.id)
            }
        }
    }    
}
    
    


</script>

<style lang="scss" scoped >
/* Dropdown transition */
.fade-enter-from {
    opacity: 0;
}
.fade-enter-to {
    opacity: 1;
}
.fade-enter-active {
    transition: all 1s ease;
}
.fade-leave-from {}
.fade-leave-to {}
.fade-leave-active {}


.header-row {
position: relative;
display: flex;
justify-content: space-between;
}
#title {
    font-size: 16px;
    font-weight: 800;
    color: #fff;
    display:inline-block;
    width: 50%;
}
.view-details {
    display: inline-block;
    position: absolute;
    left: 50%;
    border-radius: 50px;
    width: 80px;
    font-size: 11px;
    font-weight: 500;
    margin: 15px;
    text-align: center;
    color: $p-grey;
    transition: box-shadow 400ms;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
    transition: all 200ms ease-in-out;
    cursor: pointer;
}


.priority {
    display:inline-block;
    font-size: 15px;
    color: $dark-grey;
    width: 100px;
}
.status-container {
    margin: 13px;
    
  
    
}
.entry-container {
 
 box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
-webkit-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
-moz-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
 margin: 25px;
 background-color: $background-color-2;
 border: 1px solid $border-color-1;
 transition: border-color 500ms ease;
}

.entry-wrapper {
    padding-left: 25px;
    padding-right: 25px;
}

.dropdown-container {
    color: $dark-grey;
}
.time-stamp {
    font-size: 11px;
    color: $dark-grey;
    border-bottom: solid 1px $border-color-2;
    display: flex;
}
.time-stamp p{
    margin-right: 20px;
}

.footer {
    text-align: center;
    background-color: $border-color-1;
    font-size: 11px;
    color: $white;
    transition: all 500ms ease;
 
}
.footer p{
    margin: 0;
    font-weight: 500;
}
.footer:hover {
    background-color: $border-color;
    color: $border-color-1;
    cursor: pointer;
}
.button {
    cursor: pointer;
    margin-right: 20px;
    
}
.button-container {
    display: flex;
    flex-wrap: nowrap;
    margin-bottom: 15px;
    
}
.countdown-container {
    width: 100px;
}
.space {
    
}

</style>