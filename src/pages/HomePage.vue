<template>
  <div id="home-page">
      <h1> Trending </h1>
      <!-- a select button for algorithm picker -->
      <!-- <b-form-select v-model="selected" :options="algorithms"></b-form-select> -->
      <Card :infos=infos></Card>
  </div>
</template>

<script>
import Card from "./../components/Card.vue"
export default {
    name: "HomePage",
    components:{
        Card,
    },
    props: {
        algorithms:{
            type: Array,
            required: true
        }
    },
    data(){
        return{
            selected: null,
            infos: [
                {
                    title: "bla",
                },
                {
                    title: "bla2"
                },
                {
                    title: "bla3"
                }
            ]
        }
    }
}
</script>

<style>
#home-page{
    text-align: center;
}
</style>