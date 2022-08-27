<template>
        <div class="list-wrapper">
            <div>
            <div class="table-row" v-for="(task, index) in ticketListData" :key="index.id">
                 <TicketComponent 
                 :index="index"
                 :title="ticketListData[index].title"
                 :content="ticketListData[index].content"
                 :timestamp="ticketListData[index].timestamp"
                 :dateToComplete="ticketListData[index].dateToComplete"
                 :status="ticketListData[index].status"
                 :id="ticketListData[index].id"
                 :priority="ticketListData[index].priority"
                 :createdBy="ticketListData[index].createdBy"
                 />
            </div>
            </div>
        </div>
</template>

<script>
import TicketComponent from './TicketComponent.vue';
export default {
    name: "ListTaskComponent",
    components: {
    TicketComponent
    },
    data(){
        return {
            ticketList: []
        }
    },
    computed: {
        ticketListData(){
            // Reverse the list so that newest ticket is displayed
            return this.$store.state.ticketList.slice().reverse();
        }
    },   
}
</script>


<style lang="scss" scoped > 
.list-wrapper {
    height: 100%;
 
   
    overflow-y: hidden;
    /*background-color: $background-color;*/

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