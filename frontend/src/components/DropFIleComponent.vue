<template>


    <div id="containerr"  
    @dragenter.prevent="toggleActive" 
    @dragleave.prevent="toggleActive" 
    @dragover.prevent 
    @drop.prevent="toggleActive"
    :class="{ 'active-droparea': active}">
        <div id="image_drop_area" @drop.prevent="onDrop" @change="selectedFile">

            
            <input type="file" id="drop-file-input" class="hidden" multiple @change="uploadFile" accept="image/png, image/jpg">
            <label for="drop-file-input">Drag and drop image file here</label>
            <span class="file-detail">{{dropFile.name}}</span>
          
            <div id="display-image"></div>
        </div>
    </div>

</template>
    
<script>
import { ref } from 'vue';


export default {
    name: "DropFileComponent",

    setup(){
        let dropFile = ref("");
        const active = ref(false);

        const selectedFile = () => {
            dropFile.value = document.getElementById("drop-file-input").files[0]
        }
        const onDrop = (event) => {
            dropFile.value = event.dataTransfer.files[0]
            var reader = new FileReader();
            var preview = document.getElementById("display-image")
            reader.onload = function(readerEvent){
                var listItem = document.createElement("li");
                listItem.innerHTML = "<img src='" + readerEvent.target.result + "' />";
                preview.append(listItem)
            }
            
            var image = reader.readAsDataURL(dropFile.value)
            console.log(reader.readAsDataURL(dropFile.value))
            document.getElementById("display-image").style.backgroundImage = "url(" + image + ")";
            
            
        }
        const toggleActive = () => {
            active.value = !active.value;
        }
        return {
            dropFile, active, toggleActive, onDrop, selectedFile
        }
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
#drop-file-input {
    
    display: none;
}
label {
     color: $white;
     cursor: pointer;
}
.active-droparea {
    background-color: $border-color-2;
    

}



</style>