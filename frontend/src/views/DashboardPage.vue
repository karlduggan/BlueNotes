<template>
<div v-if="this.$store.state.isAuthenticated">
    <div class="container">
      <div class="inner-container">
        <div class="inner-left-container">
         
          <button id="create-project" class="btns" @click="createProjectToggle">Create Project</button>
          <button id="delete-project" class="btns">Delete Project</button>    
          
        </div>
        <div class="inner-right-container">
          <div class="inner-right-top-container">
            <div class="stat-container-1">
              Stat 1 Section
            </div>
            <div class="stat-container-2">
              Stat 2 Section
            </div>
          </div>
          <div class="inner-right-bottom-container">
            <!--Test Project Component Below-->
            <ProjectListComponent/>
          </div>
        </div>
      </div>
      <transition name="fade" >
            <div v-if="this.$store.state.createProjectDisplay">
               <div class="create-project-modal-container">
                <h1>Create Project Modal Container</h1>
               </div>      
            </div>
            
        </transition>
    </div>

    
</div>
    
</template>
<script>
import axios from 'axios'
import ProjectListComponent from '@/components/ProjectListComponent.vue'
export default{
    name: "DashboardPage",
    data() {
        return {};
    },
    beforeCreate() {
        this.$store.commit("initializeStore");
        const token = this.$store.state.token;
        if (token) {
            axios.defaults.headers.common["Authorization"] = "Token " + token;
        }
        else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    created() {
        // Work around to have a persistent data and to not loose the username when refreshing the page 
        this.$store.state.username = localStorage.getItem("username");
    },
    components: { ProjectListComponent },
    methods: {
      createProjectToggle: function(){
        this.$store.state.createProjectDisplay = !this.$store.state.createProjectDisplay;
        console.log(this.$store.state.createProjectDisplay)
      }    }
}
</script>
<style lang="scss" scoped>

.container{
background-color: $background-color;
// Off set the header with calc 
   min-height: calc(100vh - 68px);

 }
.inner-container{


display: flex;
flex-direction: row;
flex-wrap: nowrap;
justify-content: normal;
align-items: stretch;
align-content: stretch;
height: 100%;
}
.inner-left-container{
border-right: 1px solid $border-color-2;
padding: 15px;
display: flex;
display: block;
flex-grow: 1;
flex-shrink: 1;
flex-basis: auto;
align-self: auto;
order: 0;
max-width: 12em;
min-width: 12em;

}
.inner-right-container{

padding: 5px;
display: block;
flex-grow: 15;
flex-shrink: 0;
flex-basis: auto;
align-self: stretch;
order: 0;
flex-direction: column;

// Off set the header with calc 
   min-height: calc(100vh - 68px);
display: flex;
flex-direction: column;
flex-wrap: nowrap;
justify-content: normal;
align-items: stretch;
align-content: stretch;
}
.inner-right-top-container{

height: 300px;
display: flex;
flex-direction: row;
flex-grow: 0;
flex-shrink: 0;
flex-basis: auto;
align-self: stretch;
order: 0;
}
.stat-container-1{
  border: 1px solid $border-color-2;
  margin: 5px;
  display: block;
  flex-grow: 2;
  flex-shrink: 0;
  flex-basis: auto;
  align-self: stretch;
  order: 0;
  
}
.stat-container-2{
  border: 1px solid $border-color-2;
  margin: 5px;
  display: block;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
  align-self: stretch;
  order: 0;
}
.inner-right-bottom-container{
  border: 1px solid $border-color-2;
  margin: 5px;
  
  display: block;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
  align-self: stretch;
  order: 0;
  
}
#create-project {
  background-color: transparent;
  width: 100%;
  padding: 15px;
  border: 1px solid $green;
  border-radius: 4px;
  color: $green;
  transition:all 300ms ease-in-out;
  cursor: pointer;
  font-weight: 800;
}
#create-project:hover {
  background-color: $green;
  color: $white;
}

#delete-project {
  background-color: transparent;
  width: 100%;
  padding: 15px;
  border: 1px solid $red;
  border-radius: 4px;
  color: $red;
  transition:all 300ms ease-in-out;
  cursor: pointer;
  font-weight: 800;
}
#delete-project:hover {
  background-color: $red;
  color: $white;
}
.btns {
  margin-bottom: 15px;
}

.create-project-modal-container {
  position: absolute;
 
  top: 100px;
  z-index: 10;
  width: 500px;
  height: 500px;
  background-color: pink;
}


</style>