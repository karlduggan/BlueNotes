<template>
        <div class="list-wrapper">
            <div>
            <div class="table-row" v-for="(task, index) in taskListData" :key="index.id">
                 <EntryComponent 
                 :title="taskListData[index].title"
                 :content="taskListData[index].content"
                 :timestamp="taskListData[index].timestamp"
                 :dateToComplete="taskListData[index].dateToComplete"
                 :status="taskListData[index].status"
                 :id="taskListData[index].id"
                 :priority="taskListData[index].priority"
                 />
            </div>
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
    computed: {
        taskListData(){
            return this.$store.state.taskList;
        }
    },
   
}
</script>


<style lang="scss" scoped >
.list-wrapper {
    height: 740px;
    width: 850px;
    overflow-y: hidden;
    background-color: $background-color;

}
.list-wrapper:hover {
    overflow: auto;
    overflow: overlay;
}
.list-wrapper::-webkit-scrollbar {
    background-color: $background-color-4;
    position: absolute;
}




</style>