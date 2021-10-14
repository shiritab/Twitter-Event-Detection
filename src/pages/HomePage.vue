<template>
  <div id="home-page">
      <h1> Trending </h1>
      <br>
      
      <!-- a select button for algorithm picker -->
      <b-form-select style="width:20%" v-model="selected" :options="['SEDTWik', 'twembeddings', 'algorithm 3','algorithm 4']"></b-form-select>
      <Graph></Graph>


  </div>
</template>

<script>
import Graph from "../components/graph.vue"
export default {
    name: "HomePage",
    components:{
        Graph
        
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
            ],


        }
    }
}
</script>

<style>
#home-page{
    text-align: center;
}
#charts{
    margin-top: 3%;
    margin-left: 2%;
    display:flex;
}
</style>