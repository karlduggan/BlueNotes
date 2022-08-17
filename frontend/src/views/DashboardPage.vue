<template>
<div v-if="this.$store.state.isAuthenticated">
    <div class="container">
      <div class="inner-container">
        <div class="inner-left-container">
          Button Item section
          <h2>Dashboard</h2>
          <button>Create Project</button>
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
            Project List Section
          </div>
        </div>
      </div>
    </div>

    
</div>
    
</template>
<script>
import axios from 'axios'
export default{
    name: 'DashboardPage',
    data(){
        return {

        }
    },
    beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if(token){
    axios.defaults.headers.common['Authorization'] = "Token " + token
  }  else {
    axios.defaults.headers.common['Authorization'] = ''
  }
},
created(){
  // Work around to have a persistent data and to not loose the username when refreshing the page 
  this.$store.state.username = localStorage.getItem('username')
},
}
</script>
<style lang="scss" scoped>

 .container{

height: 800px;

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
display: flex;
display: block;
flex-grow: 1;
flex-shrink: 1;
flex-basis: auto;
align-self: auto;
order: 0;

}
.inner-right-container{

padding: 10px;
display: block;
flex-grow: 6;
flex-shrink: 0;
flex-basis: auto;
align-self: stretch;
order: 0;

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


</style>