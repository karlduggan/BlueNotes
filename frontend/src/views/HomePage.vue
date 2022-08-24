<template>
    <body>
        <div class="hero-banner">
            <h1>BluNotes</h1>

            <h2>A simple ticket management system with a minimalistic design, 
                built for the sole purpose of helping you get things done</h2>
        </div>
        
    </body>

</template>

<script>
export default {
    name: 'LandingPage'
}
</script>

<style lang="scss" scoped>
body {
    background-color: $background-color;
    // Off set the header with calc 
    min-height: calc(100vh - 68px);
}
.hero-banner {
    padding: 100px;
    color: $white;
    width: 520px;
}
.hero-banner h2 {
    font-size: 18px;
}

</style>