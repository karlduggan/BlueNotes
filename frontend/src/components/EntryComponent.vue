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
                <div class="status-container">
                    <DynamicStatusButtom :status="status"/>
                </div>
                
                <!--button id="removeButton" @click="deleteEntry()">Remove</button-->
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

<style lang="scss" scoped >
.left {
    width: 100%;

}
.right {
width: 150px;
position: relative;
}
.status-container {
    position: absolute;
    bottom: 0;
    margin-bottom: 15px;
}

.container {
 width: 350px;
}
.entry {
    display: flex;
    margin-bottom: 5px;
    padding: 5px;
    width: 100%;
    border-bottom: solid 2px $light-grey;;
}
.title-container {
    font-size: 16px;
    font-weight: 800;
    color: $blue;
}

header {
    font-size: 11px;
    color: $dark-grey;
}
.content-container {
    color: $dark-grey;
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