<template>
    <div class="container">
        <tbody>
            <tr class="table-row" v-for="(task, index) in taskList" :key="index.id">
                 <EntryComponent 
                 :title="taskList[index].title"
                 :content="taskList[index].content"
                 :timestamp="taskList[index].timestamp"
                 :status="taskList[index].status"
                 />
            </tr>
        </tbody>

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
        // Testing only
        printTaskList: function() {
            console.log(this.taskList)
        }
    },
    mounted() {
        const url = "http://127.0.0.1:8000/api/task-list/";
        const options =  {
            method: 'GET',
            credentials: 'same-origin',
            
            headers: {'Content-Type': 'application/json'}}

        fetch(url, options)
            .then(response => response.json())
            .then(data => this.taskList = data)
            //.then(data => console.log(data))
            .catch( error => console.log(error.message))
            
    }
}
</script>


<style scoped>
.container {

   
}




</style>