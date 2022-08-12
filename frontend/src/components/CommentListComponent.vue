<template>
<div class="list-wrapper">
    <button @click="fetchData">Test Fetch</button>
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
            return this.$store.state.commentList;
        }
    },
    methods: {
        fetchData: async function () {
            const url = "http://127.0.0.1:8000/api/comment-list-all/";
            const options = {
                method: "GET",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Token " + this.$store.state.token
                }
            };
            let response = await fetch(url, options);
            let data = await response.json();
            console.log(data)
            this.$store.state.commentList = data;
        },
    },
    components: { CommentComponent }
}
</script>

<style lang="scss" scoped>

</style>