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

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    props: ['commentText','commentBy', 'commentDate'],
}
</script>
<style lang="scss" scoped>
p {
    color:$white;
}
.container{
background-color: $background-color;
width: 100%;
margin-bottom: 15px;
border: solid 1px $border-color-2;
border-radius: 4px;

}
.comment-wrapper{
padding: 10px;
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

}
</style>