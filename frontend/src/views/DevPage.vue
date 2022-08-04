<template>
    <div>
        <h1>Welcome to the Dev Page</h1>

        <PrioritySelectComponent></PrioritySelectComponent>
    </div>

</template>

<script>
import PrioritySelectComponent from '@/components/PrioritySelectComponent.vue'


export default {
    setup() {
        return {
            
        }
    },
    components: {
    PrioritySelectComponent
},
    name: 'DevPage',
    data() {
        return {
       
        }
    },
    methods: {
        
}
}
</script>

<style lang="scss" scoped>

</style>