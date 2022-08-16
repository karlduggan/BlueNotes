<template>
<div v-if="this.$store.state.isAuthenticated">
    <h1>Dashboard Temp</h1>
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
</style>