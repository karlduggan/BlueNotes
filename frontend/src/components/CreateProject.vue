<template>

<div class="create-project-container">
    <div class="close-header" @click="closeModalAction">X</div>
    <div class="wrapper">

    
        <header>
            <h1>New Project</h1>
        </header>
        <body>
            <input type="text" v-model="project_title" placeholder="Project Title..."/>
            <textarea type="text" v-model="project_detail" placeholder="Project Detail..."/>
        
            <button class="create-project-btn" @click="createProjectAction">Add Project</button> 
            
        </body>
    </div>
    
</div>
</template>

<script>
import axios from 'axios';
export default {
    name: "CreateProject",
    data(){
        return {
            project_title: "",
            project_detail: ""
        }
    },
    methods:{
        clearFields: function() {
            this.project_title = "";
            this.project_detail = "";
        },
        getTimeStamp: function(){
            return "temp time stamp"
        },
        createProjectAction: function(){
            /*
            title = models.CharField(max_length=100)
            createdBy = models.CharField(max_length=100)
            content = models.TextField(max_length=1000, default='None')
            timestamp = models.CharField(max_length=100, default="None")
            */
           const url = "http://127.0.0.1:8000/api/project-create/"
            const data = {
                "title": this.project_title,
                "content": this.project_detail,
                "createdBy": this.$store.state.username,
                "timestamp": this.getTimeStamp()
            }

            axios.post(url, data, {
                headers: {'Authorization': 'Token ' + this.$store.state.token}
            })
            console.log(data)
            this.clearFields()
            // Close the Create Project Modal display
            this.closeModalAction();
        },
        closeModalAction: function() {
            // Close the Create Project Modal display
            this.$store.state.createProjectDisplay = false;
        }
    }

}
</script>

<style lang="scss" scoped>
.create-project-container{
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    align-items: center;
    top: 100px;
    z-index: 10;
    width: 500px;
   
    
    background-color: $background-color;
    border-radius: 4px;
    border: solid 1px $green;
    -webkit-box-shadow: 5px 5px 15px 5px #000000; 
    box-shadow: 5px 5px 15px 5px #000000;
    color: $green;
}
.wrapper {
 padding: 25px;
}
header {
    text-align: center;
}
body {
    display: flex;
    flex-direction: column;
}
input {
    padding: 10px;
    font-size: 18px;
    border: none;
    background-color: $border-color-1;
    color: #fff;
    border-radius: 4px;
    outline: none;
}

input::placeholder {
    color: $background-color;
}
textarea {
    padding: 10px;
    margin-top: 15px;
    font-size: 14px;
    font-family: sans-serif;
    border: none;
    background-color: $border-color-2;
    color: $white;
    border-radius: 4px;
    outline: none;
    height: 80px;
    resize: none;
    transition: border-color 500ms ease;
}
textarea::placeholder {
    color: $background-color;
}

.create-project-btn {
    display: block;
    flex-grow: 1;
    padding: 15px;
    margin-top: 35px;
    border: solid $green 1px;
    border-radius: 5px;
    background-color: transparent;
    font-weight: 800;
    color: $green;
    cursor: pointer;
    transition: all 300ms ease-in-out;
}
.create-project-btn:hover {
    background-color: $green;
    border: solid $green 1px;
    color: $white;
}
.close-header {

    position: absolute;
    right: 5px;
    padding: 5px;
    color: $green;
    font-weight: 500;
    cursor: pointer;

}

</style>