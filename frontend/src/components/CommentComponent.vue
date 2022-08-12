<template>
    <div>
        <div class="container">
            <div class="comment-wrapper">
                <div class="header">
                    <span><p>{{commentBy}}</p><p>{{commentDate}}</p></span>
    
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

}
.comment-wrapper{

}
.header{

}
.body{

}
.footer{

}
</style>