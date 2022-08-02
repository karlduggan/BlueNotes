<template>
    <div class="container">
        <div class="inside-container">
                <input type="text" v-model="title" placeholder="Title..."/>
                <textarea type="text" v-model="content" placeholder="More Detail..."/>  
                <button @click="CreateTask()">Submit</button>
        </div>
    </div>
</template>

<script>

export default {
    data(){
        return {
            title: "",
            content: ""
        }
    },
    methods: {
        formatInput: function(string){
        // This method will return the same string with the first letter uppercased
        return string.charAt(0).toUpperCase() + string.slice(1);
        },

        CreateTask: function(){
            var data = {
                "id": "1", 
                "title": this.formatInput(this.title), 
                "content": this.formatInput(this.content), 
                "completed": "False", 
                "status": "To Do",
                "timestamp": this.timeStamp()
            };
            console.log(this.title)

            const url = "http://127.0.0.1:8000/api/task-create/"
            fetch(url, {
                method: 'POST',
                credentials: 'same-origin',
                body: JSON.stringify(data),
                headers: {
                    'Content-type': 'application/json; charset=UTF-8',
                },
               
            })
            .then((response) => response.json())
            .then((data) => {
                console.log('Success: ', data);
            })
            .catch((error) => {
                console.log('Error: ', error);
            });
            // Clear text input fields
            this.title = "";
            this.content = "";
        },
        timeStamp: function(){
        var d = new Date();
        //Hour
        var year = d.getFullYear();
        var month = d.getMonth();
        var day = d.getDate();
        var hour = d.getHours();
        var minute = d.getMinutes();
        var seconds = d.getSeconds();

        return `${hour}:${minute}:${seconds} ${day}-${month}-${year}`;

    }
        

    },
   
}
</script>

<style lang="scss" scoped>

.container {
    width: 430px;
    padding: 10px;
}
.inside-container {
    width: 100%;
    padding: 10px;

    position: relative;
    box-sizing: border-box;
}
input {
    padding: 10px;
    width: 100%;
    font-size: 18px;
    border: solid $light-grey 3px;
    color: $dark-grey;
    outline: none;
    position: relative;
    box-sizing: border-box;
}
textarea {
    padding: 10px;
    margin-top: 15px;
    box-sizing: border-box;
    width:100%;
    font-size: 14px;
    font-family: sans-serif;
    border: solid $light-grey 3px;
    color: $dark-grey;
    outline: none;
    height: 80px;
    resize: none;


}
button {
    width: 100%;
    padding: 15px;
    margin-top: 15px;
    border: solid $light-grey 3px;
    background-color: $light-grey;
    font-weight: 800;
    color: $dark-grey;
    cursor: pointer;
}
button:hover {
    background-color: $dark-grey;
    border: solid $dark-grey 3px;
    color: $white;
}
</style>