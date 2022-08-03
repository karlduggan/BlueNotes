<template>
    <div>
        <h1>Welcome to the Dev Page</h1>


        <Datepicker v-model="date"></Datepicker>
        <button @click="getDate">Click</button>
    </div>

</template>

<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default {
    setup() {
        return {
            
        }
    },
    components: {
        Datepicker
    },
    name: 'DevPage',
    data() {
        return {
            date: null,
        }
    },
    methods: {
        getDate: function() {
            console.log(this.date);
        }
    }
}
</script>

<style lang="scss" scoped>

</style>