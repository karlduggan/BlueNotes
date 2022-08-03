<template>
    <div>
        <h1>Welcome to the Dev Page</h1>

        <input v-model="dateSelected" type="date" id="calendar" name="birthday">
        <button @click="getDate">Click</button>
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
            dateSelected: ""
        }
    },
    methods: {
        getDate: function() {
            console.log(this.dateSelected);
        }
    }
}
</script>

<style lang="scss" scoped>

</style>