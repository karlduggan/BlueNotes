<template>
<div class="list-wrapper">
            <div>
                <div class="table-row" v-for="(comment, index) in commentListData" :key="index.id">
                    <!---Put data format here for comment-->
                </div>
            </div>
        </div>
</template>

<script>
export default {
    name:"CommentListComponent",
    computed:{
        commentListData() {
            return this.$store.state.commentList
        }
    },

    methods: {
        fetchData: async function(){
            const url = "http://127.0.0.1:8000/api/comment-list-all/";
            const options =  {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Token ' + this.$store.state.token
            }}
            let response = await fetch(url, options);
            let data = await response.json()
            this.$store.state.commentList = data;
          
        },
    },
}
</script>

<style lang="scss" scoped>

</style>