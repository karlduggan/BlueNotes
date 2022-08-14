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
    display: flex;
   justify-content: center;
   // Off set the header with calc 
   min-height: calc(100vh - 68px);

}
.container {
    position: absolute;
    top: 150px;
}

</style>