<template>
    <div class="container" @click="redirectToProjectPage">
        
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
    },
    methods:{
        redirectToProjectPage: function(){
            console.log(this.id)
            // Assign project selected id to the stored state
            this.$store.state.selectedProjectID = this.id
            // store selected project id to the locaStorage
            localStorage.setItem("projectID", this.id);
            // Redirect to the ticket list of the selected project
            this.$router.push("/todo-list");
        }
    }
}
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    margin: 25px;
    width: 300px;
    height: 200px;
    border-radius: 4px;
    background-color: $border-color-2;
    cursor: pointer;
    box-sizing: content-box;
    border: solid 1px $green;
    box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
    -webkit-box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px 10px 6px -3px rgba(0,0,0,0.75);
    color: $white;
}
.container 
.right{
    padding: 15px;
}

footer {
    display: flex;
}
</style>
