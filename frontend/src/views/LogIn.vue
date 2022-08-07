<template>
    <body>
        <div class="container">
            <LoginFormComponent/>
        </div>
    </body>
</template>

<script>

import LoginFormComponent from '@/components/LoginFormComponent.vue'

export default {
    name: "LogIn",
    data() {
        return {
        
        };
    },
    methods: {

    },
    components: { LoginFormComponent }
}
</script>

<style lang="scss" scoped>
body {
    background-color: $background-color;
    min-height: 90vh;
    display: flex;
   justify-content: center;
}
.container {
    position: absolute;
    top: 150px;
}

</style>