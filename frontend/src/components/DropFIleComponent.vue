<template>

<div class="container">
    <p>Drag and drop an image into the box</p>
    <div id="image_drop_area"></div>
</div>
</template>
    
<script>
export default {
    name: "DropFileComponent",
    data(){

    },
    methods: {
        
    }
}
</script>

<style lang="scss">
#image_drop_area{
   width: 400px;
   height: 225px;
   border: 1px solid black;
   background-position: center;
   background-size: cover;
   box-sizing: border-box;  
}

</style>