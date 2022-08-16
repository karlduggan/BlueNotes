<template>
  <div ref="draggableContainer" id="draggable-container">
    <div id="draggable-header" @mousedown="dragMouseDown">
    </div>
    <body>
        <CreateTaskComponent></CreateTaskComponent>
    </body>
    <footer>

    </footer>
  </div>
</template>

<script>
import CreateTaskComponent from './CreateTaskComponent.vue'
export default {
    name: "CreateTicket",
    data: function () {
        return {
            positions: {
                clientX: undefined,
                clientY: undefined,
                movementX: 0,
                movementY: 0
            }
        };
    },
    methods: {
        dragMouseDown: function (event) {
            event.preventDefault();
            // get the mouse cursor position at startup:
            this.positions.clientX = event.clientX;
            this.positions.clientY = event.clientY;
            document.onmousemove = this.elementDrag;
            document.onmouseup = this.closeDragElement;
        },
        elementDrag: function (event) {
            event.preventDefault();
            this.positions.movementX = this.positions.clientX - event.clientX;
            this.positions.movementY = this.positions.clientY - event.clientY;
            this.positions.clientX = event.clientX;
            this.positions.clientY = event.clientY;
            // set the element's new position:
            this.$refs.draggableContainer.style.top = (this.$refs.draggableContainer.offsetTop - this.positions.movementY) + "px";
            this.$refs.draggableContainer.style.left = (this.$refs.draggableContainer.offsetLeft - this.positions.movementX) + "px";
        },
        closeDragElement() {
            document.onmouseup = null;
            document.onmousemove = null;
        }
    },
    components: { CreateTaskComponent }
}
</script>

<style lang="scss" scoped>
#draggable-container {
  position: absolute;
  top: 20%;
  z-index: 9;
  background-color: $background-color-2;
  border-radius: 4px;
  border: 1px solid $border-color-1;


      box-shadow: 1px 5px 20px rgb(0 0 0 / 50%);
    -webkit-box-shadow: 1px 5px 20px rgb(0 0 0 / 50%);
}
body {
    padding: 15px;
}
#draggable-header {
  z-index: 10;
  cursor:move;
  height: 20px;
  background-color: $border-color-2;
  position: relative;
}
</style>