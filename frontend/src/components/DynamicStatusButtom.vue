<template>
    <div >
        <div 
        class="button"
        :style="{backgroundColor: currentColor}"
        @click="changeStatus" >{{currentStatus}}</div>
    </div>
</template>


<script>

export default {
    props : {
        status: String,
        entryId: Number
    },
    data() {
        return {
            currentStatus: this.status,
            currentColor: "#727CF5",
            changesMade : false,
            updateActive: false,
            updateIntervalDuration: 3000
        }
    },
    methods: {
        // On click change the status
        changeStatus: function() {
            this.updateStatusChange(this.currentStatus);
        },
        runUpdate: function() {
         
            
        },
        updateStatusChange: function(currentStatus) {
            const updateStatus = { 
                "To Do": "In Progress", 
                "In Progress": "Completed",
                "Completed": "Overdue",
                "Overdue": "To Do"
            };
            // Set and update status
            this.currentStatus = updateStatus[currentStatus];
            console.log(this.entryId)
            this.runUpdate()
            // Background color update
            switch(this.currentStatus){
                case "To Do":
                    // Blue
                    this.currentColor = "#727CF5";
                    break;
                case "In Progress":
                    // Purple
                    this.currentColor = "#CC7EDF";
                    break;
                case "Completed":
                    // Green
                    this.currentColor = "#3CC479";
                    break;
                case "Overdue":
                    // Red
                    this.currentColor = "#EF4E58";
                    break;
    }

    }
}

}

</script>

<style lang="scss" scoped>
.button {
    font-family: sans-serif;
    font-size: 12px;
    border: none;
    width: 75px;;
    padding: 5px;
    cursor: pointer;
    text-align: center;
    align-content: center;
    border-radius: 4px;
    color: $white;
    font-weight: 500;
}

</style>