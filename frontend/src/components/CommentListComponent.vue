<template>
<div class="list-wrapper">
    
            <div>
                <div class="table-row" v-for="(comment, index) in commentListData" :key="index.id">
                    <!---Put data format here for comment-->
                    <CommentComponent
                    :id="commentListData[index].id"
                    :commentText="commentListData[index].comment"
                    :commentBy="commentListData[index].createdBy" 
                    :commentDate="'date needed'"></CommentComponent>
                </div>
            </div>
        </div>
</template>

<script>
import CommentComponent from './CommentComponent.vue';
export default {
    name: "CommentListComponent",
    computed: {
        commentListData() {
            // Reverse the list so that newest comment is displayed
            return this.$store.state.commentList.slice().reverse();
        }
    },
    methods: {
       
    },
    components: { CommentComponent }
}
</script>

<style lang="scss" scoped>
.list-wrapper {
    height: 100%;  
  
    margin-top: 15px;   
    overflow-y: hidden; 
    
}
.list-wrapper:hover {
    overflow: auto;
    overflow: overlay;
}
.list-wrapper::-webkit-scrollbar {
    background-color: $background-color-2;
    position: absolute;
    width: 10px
}
.list-wrapper::-webkit-scrollbar-thumb {
  background-color: $background-color-4;
  
  border-radius: 25px;
}

</style>