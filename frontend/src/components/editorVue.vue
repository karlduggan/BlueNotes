<template>
<div>

<!-- Create the editor container -->
<div id="editor">
  <p>Hello World!</p>
  <p>Some initial <strong>bold</strong> text</p>
  <p><br></p>
</div>

<!-- Include the Quill library -->

</div>

</template>

<script>

    export default {
        name: "editorVue",
        props: {
            value: {
                type: String,
                default: ''
            }
        }, 

            }
</script>

<style scoped>
</style>