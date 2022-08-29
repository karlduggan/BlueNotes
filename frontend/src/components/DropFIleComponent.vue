<template>


    <div id="containerr"  @dragover.prevent @drop.prevent>
        <div id="image_drop_area" @drop="onDrop">
            <p>Drag and drop image file here</p>
            <input type="file" id="fileElm" multiple @change="uploadFile">
            <div v-if="fileUpload.length > 0" class="image-div">
                <div v-for="file in fileUpload" :key="file.src">
                    <img :src="file.src" class="image" />
                </div>
            </div>
        </div>
    </div>

</template>
    
<script>
export default {
    name: "DropFileComponent",
    data(){
        return {
        fileUpload: []
        }
    },
    methods: {
        uploadFile: function(event){
            this.fileUpload = event.target.files;
            console.log("File uploaded")
           
        },
        onDrop: function(event){
            this.fileUpload = event.dataTransfer.files;
            console.log("Item dropped !")
            console.log(event.dataTransfer.files[0])
          
        }
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
input {
    color: $white;
}


</style>