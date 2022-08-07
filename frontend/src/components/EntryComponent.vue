<template>
    <div class="entry-container">

        <div class="entry-wrapper">

                <!-- Header Row STARTS-->
                <div class="header-row">
                    <div id="title"><p>{{title}}</p></div>

                    <!-- View Details BTN STARTS -->
                    <div class="view-details" @click="showDrop = !showDrop">
                        <p>View Details</p>

                    </div>
                    <!-- View Details BTN ENDS -->

                    <!-- Priority STARTS -->
                    <div class="priority">
                        <p>{{priority}}</p>
                    </div>
                    <!-- Priority ENDS -->

                    
                 
                 
                    
                    <div class="status-container">
                        <DynamicStatusButtom :status="status"/>
                    </div>
                </div>
                <!-- Header Row ENDS -->

                
                <!-- Dropdown Container BEGINS -->
                <transition name="fade">
                    <div v-if="showDrop" class="dropdown-container">

                        <div class="time-stamp">
                            <p>{{timestamp}}</p>
                        </div>
                        <div class="content-container">
                            <p>{{content}}</p>
                        </div>
                    </div>
                </transition>
                <!-- Dropdown Container ENDS -->
            </div>    
                
                <!--button id="removeButton" @click="deleteEntry()">Remove</button-->
    </div>
</template>

<script>
import { ref } from 'vue';
import DynamicStatusButtom from './DynamicStatusButtom.vue'

export default {
    setup(){
        const showDrop = ref(false);
        return {
            showDrop
        }
    },
    name: "EntryComponent",
    props: [
        'id',
        'title',
        'content',
        'status', 
        'timestamp',
        'dateToComplete',
        'priority'
    ],
    components: {
    DynamicStatusButtom
},
    data(){
        return {
            

        }
    },
    methods: {
        deleteEntry: function(){
         

            const url = "http://127.0.0.1:8000/api/task-delete/" + this.id;
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
}
#title {
    font-size: 16px;
    font-weight: 800;
    color: #fff;
    display:inline-block;
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
.view-details p {
    margin: 0;
    padding: 5px;
}
.view-details:hover {
    color: #fff;
    background-color: $blue;
    transition: all 200ms ease-in-out;
    
}

.priority {
    display:inline-block;
    font-size: 11px;
    color: $dark-grey;
    position:absolute;
    left: 67%;
    margin: 10px;
}
.status-container {
    margin: 13px;
    position: relative;
    float: right;
    
}
.entry-container {
 padding: 5px;
 box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
-webkit-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
-moz-box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.5)  ; 
 margin: 25px;
 background-color: $background-color-2;
 border: 1px solid $border-color-1;
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
}
#removeButton {
    font-family: sans-serif;
    border: none;
    width: 100px;;
    padding: 5px;
    cursor: pointer;
    text-align: center;
    align-content: center;
    margin-top: 10px;
}


</style>