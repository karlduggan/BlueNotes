<template>
<div class="container-project-list">
    <ProjectComponent 
    id="1"
    title="Project Name"
    summary="This is where the summary goes"
    createdBy="Karl"
    dateCreated="19/02/1988"/>
    <ProjectComponent 
    id="1"
    title="Project Name 2"
    summary="This is where the summary goes"
    createdBy="Karl"
    dateCreated="19/02/1988"/>
</div>

</template>

<script>
import ProjectComponent from './ProjectComponent.vue';
export default {
    name: "ProjectListComponent",
    data() {
        return {};
    },
    components: { ProjectComponent }
}
</script>

<style lang="scss" scoped>
.container-project-list {
    display: flex;
    flex-wrap: wrap;
}

</style>