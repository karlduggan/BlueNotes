<template>


    
    <div id="image_drop_area">
        <p>Drag and drop image file here</p>
        
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
    margin-top: 15px;
   width: 100%;
   height: 200px;
   border: 1px dashed $border-color-2;
   background-position: center;
   background-size: cover;
   box-sizing: border-box;  
   text-align: center;
   
   
}
#image_drop_area p {
   
    color: $border-color-2;
}

</style>