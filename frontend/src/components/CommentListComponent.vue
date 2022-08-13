<template>
<div class="list-wrapper">
    
            <div>
                <div class="table-row" v-for="(comment, index) in commentListData" :key="index.id">
                    <!---Put data format here for comment-->
                    <CommentComponent
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

</style>