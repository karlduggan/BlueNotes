<template>
    <div class="container">
        <div class="list-wrapper">
            <tbody>
            <tr class="table-row" v-for="(task, index) in taskList" :key="index.id">
                 <EntryComponent 
                 :title="taskList[index].title"
                 :content="taskList[index].content"
                 :timestamp="taskList[index].timestamp"
                 :status="taskList[index].status"
                 :id="taskList[index].id"
                 />
            </tr>
            </tbody>
        </div>
        

    </div>
</template>

<script>
import EntryComponent from './EntryComponent.vue';
export default {
    name: "ListTaskComponent",
    components: {
    EntryComponent
},
    data(){
        return {
            taskList: []
        }
    },
    methods: {
        updateTaskList: function(){
            const url = "http://127.0.0.1:8000/api/task-list/";
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {'Content-Type': 'application/json'
            }}
            fetch(url, options)
            .then(response => response.json())
            .then(data => this.taskList = data)
            .catch( error => console.log(error.message))

            // Reverse the task list 
            this.taskList = this.taskList.reverse();
        }
        
    },
   
    mounted() {
        this.updateTaskList()
    }
}
</script>


<style scoped>
.container {

   
}
.list-wrapper {
    height: 500px;
    width: 365px;
    overflow-y: hidden;
    padding: 20px;
    border: solid rgb(229, 229, 229) 3px;
}
.list-wrapper:hover {
    overflow-y: scroll;
}




</style>