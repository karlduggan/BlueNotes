<template>
    <div>
        <div class="container">
            <div class="comment-wrapper">
                <div class="header">
                    <p>Comment by: <b>{{commentBy}}</b></p>
                    <span class="header-date-created"><p>{{commentDate}}</p></span>
    
                </div>
                <div class="body">
                    <p>{{commentText}}</p>
                </div>
                <div class="footer">
                    <button>Edit</button>
                    <button @click="deleteComment">Delete</button> 
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
export default{
    props: ['commentText','commentBy', 'commentDate', 'id'],
    methods: {
        'deleteComment': function(){
            console.log(this.id )
            let confirmation = confirm("Are you sure you want to delete comment?")
            if(confirmation == true){
                const url_delete = "http://127.0.0.1:8000/api/comment-delete/" + this.id;
                axios.delete(url_delete)
                .then(console.log('Delete Successful')).catch(error => (console.error("Error occured with when trying to delete a comment: ", error)))
                this.$store.state.commentList.pop(this.id)
                // Get and refresh ticket list
                //const url_get = "http://127.0.0.1:8000/api/comment-list/" + this.$store.state.selectedTicketID;
                //axios(url_get).then(data => (this.$store.state.commentList = data))
            }
        
            }
            
    },
}
</script>
<style lang="scss" scoped>
p {
    color:$white;
}
.container{
background-color: $background-color;
width: 300px;
margin-bottom: 15px;
border: solid 1px $border-color-2;
border-radius: 4px;

}
.comment-wrapper{
padding: 10px;
white-space: initial;
}
.header{
border-bottom: solid 1px $border-color-2;
padding: 5px;


}
.header p{
display: inline;
color: $p-text;
font-size: 14px;
}
.header-date-created {
    float: right;
}
.body{

}
.footer{
border-top: solid 1px $border-color-2;
padding: 5px;
}
</style>