<template>
    <body>
        <div class="container">
           
            <LoginForm/>
        </div>
    </body>
</template>

<script>


import LoginForm from '@/components/LoginForm.vue';

export default {
    name: "LogIn",
    data() {
        return {
        
        };
    },
    methods: {

    },
    components: { LoginForm }
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