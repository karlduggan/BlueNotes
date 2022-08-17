<template>
    <div class="container">
        <div class="left"></div>
        <div class="right">
            <header>
                <h2>{{title}}</h2>
            </header>
            <body>
                <p>{{summary}}</p>
            </body>
            <footer>
                <span class="createdBy">{{createdBy}}</span>
                <span class="dateCreated">{{dateCreated}}</span>
            </footer>
        </div>
      
    </div>

</template>

<script>
export default {
    name: "ProjectComponent",
    props: [
        'id',
        'title',
        'summary',
        'dateCreated',
        'createdBy'
    ],
    data(){
        return {

        }
    }
}
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    margin: 15px;
    width: 230px;
   
    border-radius: 4px;
   
    background-color: $border-color-2;
    cursor: pointer;
position: relative;
    box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
    -webkit-box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
}
.left{
    background-color: #20232B;
    border-radius: 4px 0px 0px 4px;
    position: absolute;
    width: 10px;
    height: 100%;
}
.right{
    padding: 15px;
}

footer {
    display: flex;
}
</style>
