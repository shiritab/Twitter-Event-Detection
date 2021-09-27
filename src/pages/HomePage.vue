<template>
  <div>
      <h1> Trending </h1>
      <b-form-select v-model="selected" :options="algorithms"></b-form-select>
  </div>
</template>

<script>
export default {
    name: "HomePage",
    props: {
        algorithms:{
            type: Array,
            required: true
        }
    },
    data(){
        return{
            selected: null,
        }
    }
}
</script>

<style>

</style>