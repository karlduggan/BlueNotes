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
    color: $white;
    margin: 0;
    padding: 15px;
}
nav {
    background-color: $background-color-3;
    border-bottom: 1px solid $border-color-1;
    
    width: 100%;
}
</style>