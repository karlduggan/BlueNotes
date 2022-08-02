<template>
    <nav>
        <h1>{{title}}</h1>
    </nav>
</template>

<script>
export default {
    name: "NavBarComponent",
    props: {
        title: String
    }
}
</script>

<style lang="scss" scoped>
h1 {
    color: $blue;
    margin: 0;
    padding: 15px;
}
nav {
    background-color: $light-grey;
    
    width: 100%;
}
</style>