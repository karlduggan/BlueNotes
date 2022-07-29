<template>
    <div class="container">
        <div class="header">
            <h2>{{title}}</h2>
        </div>
        <div class="content-container">
            <p>{{content}}</p>
        </div>
        <button @click="statusUpdate()" >Status</button>
        <button>Delete</button>
    </div>

</template>

<script>
export default {
    name: "EntryComponent",
    props: {
        id: Number,
        title: String,
        content: String,
        status: String
    },
    data(){
        return {

        }
    },
    methods: {
        statusUpdate:function() {
            console.log("Testing click button for status update");
        }
    }
}
</script>

<style scoped >
.container {
    width: 300px;
    height: 300px;
    background-color: beige;
}
</style>