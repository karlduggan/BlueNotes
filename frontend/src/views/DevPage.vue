<template>
    <div>
        <h1>Welcome to the Dev Page</h1>
        <p>{{ $store.state.name}}</p>
        <p>{{ $store.state.taskList }}</p>
      <button @click="testState">Click Test</button>
      <button @click="fetchData">Click fecth data</button>
    </div>

</template>

<script>



export default {
    setup() {
        return {
            
        }
    },
    
    components: {

},
    name: 'DevPage',
    data() {
        return {
       
        }
    },
    methods: {
        testState: function(){
            this.$store.state.taskList.push('Testing');
        },
         fetchData: async function(){
            const url = "http://127.0.0.1:8000/api/task-list/";
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {'Content-Type': 'application/json'
            }}
            let response = await fetch(url, options);
            let data = await response.json()
            this.$store.state.taskList = data;
            console.log(data)
        }
},

beforeCreate(){
           
        
        },
        beforeMount(){
            this.fetchData()
        }
}

</script>

<style lang="scss" scoped>

</style>