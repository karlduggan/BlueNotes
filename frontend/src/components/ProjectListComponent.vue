<template>
<div class="container-project-list" v-for="(project, index) in projectListData" :key="index.id">
   
    <ProjectComponent 
    :id="projectListData[index].id"
    :title="projectListData[index].title"
    :summary="projectListData[index].content"
    :createdBy="projectListData[index].createdBy"
    :dateCreated="projectListData[index].timestamp"/>
</div>

</template>

<script>
import axios from 'axios';
import ProjectComponent from './ProjectComponent.vue';
export default {
    name: "ProjectListComponent",
    data() {
        return {};
    },
    computed: {
        projectListData(){
            return this.$store.state.projectList;
        }
    },
    components: { ProjectComponent },
    beforeMount(){
        const url = "http://127.0.0.1:8000/api/project-list/"
        //const options = {headers: {'Authorization': 'Token ' + this.$store.state.token}}
        console.log(this.$store.state.token)
        axios
        .get(url,{headers: {'Authorization': 'Token ' + this.$store.state.token}})
        .then((res)=>{
            this.$store.state.projectList = res.data;
            console.log(res.data);
        })

    }
}
</script>

<style lang="scss" scoped>
.container-project-list {
    display: flex;
    flex-wrap: wrap;
}

</style>