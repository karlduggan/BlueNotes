<template>
    <div class="container">
          <div class="entry">
            <div class="left">
                <header>
                        <p>{{timestamp}}</p>
                </header>
                <div class="title-container">
                    <p>{{title}}</p>
                </div>
                <div class="content-container">
                    <p>{{content}}</p>
                </div>
            </div>

            <div class="right">
                <DynamicStatusButtom :status="status"/>
                <button id="removeButton" @click="deleteEntry()">Remove</button>
            </div> 
            </div>
    </div>
</template>

<script>
import DynamicStatusButtom from './DynamicStatusButtom.vue'

export default {
    name: "EntryComponent",
    props: [
        'id',
        'title',
        'content',
        'status', 
        'timestamp'
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
            headers: {'Content-Type': 'application/json'
            }}
            fetch(url, options)
            .then(response => response.json())
            .then(data =>  console.log(data))
            .catch( error => console.log(error.message))
        }
    }

}
</script>

<style scoped >
.left {
    width: 100%;

}
.right {
width: 100px;
}
.container {
 width: 350px;
}
.entry {
    display: flex;
    margin-bottom: 5px;
    padding: 5px;
    width: 100%;
    border-bottom: solid 2px rgb(235, 235, 235);;
}
.title-container {
    font-size: 14px;
    font-weight: 800;
    color:rgb(149, 149, 149);
}

header {
    font-size: 11px;
    color:rgb(187, 187, 187);
}
.content-container {
    color:rgb(169, 169, 169);
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