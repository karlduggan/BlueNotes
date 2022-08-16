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
                    
                    <div class="buttons" title="Edit" >
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="m7 17.013 4.413-.015 9.632-9.54c.378-.378.586-.88.586-1.414s-.208-1.036-.586-1.414l-1.586-1.586c-.756-.756-2.075-.752-2.825-.003L7 12.583v4.43zM18.045 4.458l1.589 1.583-1.597 1.582-1.586-1.585 1.594-1.58zM9 13.417l6.03-5.973 1.586 1.586-6.029 5.971L9 15.006v-1.589z" fill="white"/><path d="M5 21h14c1.103 0 2-.897 2-2v-8.668l-2 2V19H8.158c-.026 0-.053.01-.079.01-.033 0-.066-.009-.1-.01H5V5h6.847l2-2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2z" fill="white"/></svg>
                    </div>
                    <div class="buttons" @click="deleteComment" title="Delete">
                         <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z" fill="white" /><path d="M9 10h2v8H9zm4 0h2v8h-2z" fill="white"/></svg>
                    </div>
                   
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
color: $white;
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
display: flex;
flex-wrap: nowrap;
}
.buttons {
    margin-right: 10px;
    cursor: pointer;
}
</style>