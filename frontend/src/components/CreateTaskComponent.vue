<template>
    <div class="container">

        <div class="inside-container">
                <input type="text" v-model="title" placeholder="Title..."/>
                <textarea type="text" v-model="content" placeholder="More Detail..."/>  
                <div class="priority-and-dates">
                    <div class="block1">
                        <PrioritySelectComponent 
                        @change="selectPriority($event)"/>
                    </div>
                    <div class="block2">
                        <Datepicker 
                        placeholder="Date to complete"
                        :enableTimePicker="false" 
                        :dark="true" 
                        calendarClassName="datepicker-class" 
                        v-model="dateSelected">
                        </Datepicker>     
                    </div>
                    
                </div>
                
                <button @click="CreateTask()">Submit</button>
        </div>
    </div>
</template>

<script>
import PrioritySelectComponent from './PrioritySelectComponent.vue';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from "vue";
export default {
    components : {
        Datepicker,
        PrioritySelectComponent,
    },
    emits: {
        'sendData': null
        },
    setup() {
        const dateSelected = ref(null);
        return {
            dateSelected
        }
    },
    data(){
        return {
            title: "",
            content: "",
            priority: "",

        }
    },
    computered: {
        taskList() {
            return this.$store.state.taskList;
        }
    },
    methods: {
        selectPriority(event) {
        this.priority = event.target.value;
        },
        getDatepickerValue: function() {
            return this.date
        },
        sendData: function(task_data){
            // task data is a dictionary
            this.$emit('sending-data', task_data)
    
        },
        formatInput: function(string){
        // This method will return the same string with the first letter uppercased
        return string.charAt(0).toUpperCase() + string.slice(1);
        },

        CreateTask: function(){
            var data = {
                "id": "1", 
                "title": this.formatInput(this.title), 
                "content": this.formatInput(this.content), 
                "completed": "False", 
                "status": "To Do",
                "timestamp": this.timeStamp(),
                "priority": this.priority,
                "dateToComplete": this.getDateToComplet()
            };
            console.log(data)
            
            // State management "store.index.js" send task data
           this.$store.state.taskList.push(data);
           
            // Send to django
            const url = "http://127.0.0.1:8000/api/task-create/"
            fetch(url, {
                method: 'POST',
                credentials: 'same-origin',
                body: JSON.stringify(data),
                headers: {
                'Content-type': 'application/json; charset=UTF-8',
                },
               
            })
            .then((response) => response.json())
            .then((data) => {
                console.log('Success: ', data);
            })
            .catch((error) => {
                console.log('Error: ', error);
            });
            // Clear text input fields
            this.title = "";
            this.content = "";
        },

        timeStamp: function(){
        var d = new Date();
        var year = d.getFullYear();
        var month = d.getMonth() + 1;
        var day = d.getDate();
        var hour = d.getHours();
        var minute = d.getMinutes();
        var seconds = d.getSeconds();

        return `${hour}:${minute}:${seconds} ${day}-${month}-${year}`;

    },
    getDateToComplet: function(){
        const ddate = this.dateSelected;
   
        return `${ddate.getDate()}-${ddate.getMonth() + 1}-${ddate.getFullYear()}`
    }
        

    },
   
}
</script>

<style lang="scss" scoped>
.priority-and-dates {
  margin-top: 10px;
  display: flex;
}
.block1 {
    display: block;
    margin-right: 10px;
}
.block2 {
    display: block;
    width: 100%;
}

.container {
 
 
}
.inside-container {
    width: 100%;
    padding: 10px;

    position: relative;
    box-sizing: border-box;
}
input {
    padding: 10px;
    width: 100%;
    font-size: 18px;
    border: solid $border-color-1 1px;
    background-color: $background-color;
    color: #fff;
    border-radius: 4px;
   
    outline: none;
    position: relative;
    box-sizing: border-box;
    transition: border-color 500ms ease;
}
input:hover {
    border-color: $border-color-hover;
    transition: border-color 500ms ease;
}
input::placeholder {
    color: $white;
}
textarea {
    padding: 10px;
    margin-top: 15px;
    box-sizing: border-box;
    width:100%;
    font-size: 14px;
    font-family: sans-serif;
    border: solid $border-color-1 1px;
    background-color: $background-color;
    color: $white;
    border-radius: 4px;
    outline: none;
    height: 80px;
    resize: none;
    transition: border-color 500ms ease;
}
textarea:hover {
    border-color: $border-color-hover;
    transition: border-color 500ms ease;
}
textarea::placeholder {
    color: $white;
}
button {
    width: 100%;
    padding: 15px;
    margin-top: 15px;
    border: solid $border-color-1 1px;
    border-radius: 5px;
    background-color: $background-color-2;
    font-weight: 800;
    color: $white;
    cursor: pointer;
}
button:hover {
    background-color: $border-color-2;
    border: solid $dark-grey 1px;
    color: $white;
}
.datepicker-class {
    background-color: $background-color-3;
    border-color: #fff;
}

</style>