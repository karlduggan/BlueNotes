<template>
    <div class="container">
        <select>
            <option value="" selected disabled hidden>Priority</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
        </select>

    </div>
</template>

<script>
export default {
    name: "PrioritySelectComponent",
    data(){
        return {

        }
    }
}
</script>

<style lang="scss" scoped>

select {
  appearance: none;
  background-color: transparent;
  border: none;
  color: $white;
  text-align: center;
  margin: 0;
  width: 100px;
  font-family: inherit;
  font-size: inherit;
  cursor: inherit;
  line-height: inherit;
  border: 1px solid $border-color-1;
  border-radius: 4px;
  transition: border-color 500ms ease;
  padding: 7px;
  
}
select:hover {
    border-color: $border-color-hover;
    transition: border-color 500ms ease;

}
select:focus {
    outline: none;
}
.container {


}

</style>