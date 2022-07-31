<template>
    <div>
        <button @click="changeStatus()" >{{currentStatus}}</button>
    </div>
</template>


<script>
export default {
    props : {
        status: String
    },
    data() {
        return {
            currentStatus: this.status
        }
    },
    methods: {
        // On click change the status
        changeStatus: function() {
            this.updateStatusChange(this.currentStatus);
        },
        updateStatusChange: function(currentStatus) {
            const updateStatus = { 
                "To Do": "In Progress", 
                "In Progress": "Completed",
                "Completed": "Overdue",
                "Overdue": "To Do"
            };
            // Set and update status
            console.log(currentStatus)
            this.currentStatus = updateStatus[currentStatus];
           


    }
}

}

</script>

<style scoped>
button {
    font-family: sans-serif;
    border: none;
    width: 100px;;
    padding: 5px;
    cursor: pointer;
    text-align: center;
    align-content: center;
}
</style>