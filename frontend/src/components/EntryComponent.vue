<template>
    <div class="container">
          <div class="entry">
                    <div class="title-container">
                        <p>{{title}}</p>
                    </div>
                    <div class="content-container">
                        <p>{{content}}</p>
                    </div>

                    
                    <span>{{timestamp}}</span>
                    <span>{{status}}</span>
                   
                </div>
    </div>
</template>

<script>

export default {
    name: "EntryComponent",
    props: [
        'title',
        'content',
        'status', 
        'timestamp'
    ],
    data(){
        return {
            

        }
    },
    methods: {
        
    }

}
</script>

<style scoped >
.container {

}
.entry {
    margin-bottom: 5px;
   
    padding: 5px;
    border: solid 2px rgb(235, 235, 235);
}
.title-container {
    font-size: 14px;
    font-weight: 800;
}


</style>