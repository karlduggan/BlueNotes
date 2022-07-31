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
        CreateTask: function(){
            var data = {
                "id": "1", 
                "title": this.title, 
                "content":this.content, 
                "completed": "False", 
                "status": "ToDO",
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

<style scoped>

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
    border: solid rgb(229, 229, 229) 3px;
    color: rgb(134, 134, 134);
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
    border: solid rgb(229, 229, 229) 3px;
    color: rgb(134, 134, 134);
    outline: none;
    height: 80px;
    resize: none;


}
button {
    width: 100%;
    padding: 15px;
    margin-top: 15px;
    border: solid rgb(229, 229, 229) 3px;
    background-color: rgb(229, 229, 229);
    font-weight: 800;
    color: rgb(134, 134, 134);
    cursor: pointer;
}
</style>