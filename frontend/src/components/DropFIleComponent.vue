<template>


    <div id="containerr"  @dragover.prevent @drop.prevent>
        <div id="image_drop_area" @drop="onDrop">

            
            <input type="file" id="fileElm" class="hidden" multiple @change="uploadFile">
            <label for="file"><p>Drag and drop image file here</p></label>
            <div v-if="fileUpload.length > 0" class="image-div">
                <div v-for="file in fileUpload" :key="file.src">
                    <img :src="file.src" class="image" />
                </div>
            </div>
        </div>
    </div>

</template>
    
<script>
// Using https://www.smashingmagazine.com/2022/03/drag-drop-file-uploader-vuejs-3/
// To learn and create drag and drop upload component
const events = ['dragenter', 'dragleave', 'dragover', 'drop']

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
            
            this.fileUpload.push(event.dataTransfer.files)
            console.log("Item dropped !")
            console.log(this.fileUpload)
          
        }
    },
    onMounted(){
        events.forEach(event => document.body.addEventListener(event, (e)=>e.preventDefault()))
    },
    onUnmounted(){
        events.forEach(event => document.body.removeEventListener(event, (e)=>e.preventDefault()))
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
#fileElm {
    color: $white;
    display: none;
}


</style>