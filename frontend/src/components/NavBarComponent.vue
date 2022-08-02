<template>
    <nav>
        <h3>{{title}}</h3>
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
h3 {
    color: $green;
    margin: 0;
}
nav {
    background-color: $light-grey;
    height: 100px;
    width: 100%;
}
</style>