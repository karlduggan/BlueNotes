<template>
<div class="container">
    <div class="wrapper">
        <textarea type="text" v-model="commentField" placeholder="Add your comment here..."/>  
    </div>
    <div class="footer">
        <button class="addCommentBTN" @click="addComment">Add Comment</button>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    props:['ticketID'],
    data(){
        return {
            commentField: "",
        }
    },
    methods:{
        addComment: function(){
            // Get Ticket id and username stored in the state
            var ticketID = this.$store.state.selectedTicketID
            var username = this.$store.state.username
            const url = "http://127.0.0.1:8000/api/comment-create/"
            const data = {
                "ticketID": ticketID,
                "comment": this.commentField,
                "createdBy": username
            }
            axios.post(url, data, {
                headers: {'Authorization': 'Token ' + this.$store.state.token}
            })
            // Append to the commentList in the state to update the frontend
            this.$store.state.commentList.push(data);
            // Clear textarea filed 
            this.commentField = ""

        }
    }
}
</script>

<style lang="scss" scoped>
.conatiner {
    width: 100%;
    padding: 10px;
    position: relative;
    box-sizing: border-box;
}
textarea{
    padding: 10px;
    
    box-sizing: border-box;
    width: 100%;
    font-size: 14px;
    font-family: sans-serif;
    border: solid $border-color-1 1px;
    background-color: $background-color;
    color: #fff;
    border-radius: 4px;
    outline: none;
    height: 80px;
    resize: none;
    transition: border-color 500ms ease;
}
textarea::placeholder {
    color: $white;
}

.addCommentBTN{
    width: 100%;
    padding: 15px;
    margin-top: 15px;
    border: solid $border-color-2 1px;
    border-radius: 5px;
    background-color: $background-color-2;
    font-weight: 800;
    color: #fff;
    cursor: pointer;
}
</style>