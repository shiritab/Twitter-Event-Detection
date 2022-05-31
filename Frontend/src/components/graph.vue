<template>
  <div id="allCharts">
      <div id="charts1">
      <!-- <Area :json_data="json_data"></Area> -->
      <Treemap :json_data="json_data"></Treemap>
      <Area :json_data="json_data"></Area>
      </div>
      <Column :json_data="json_data"></Column>

  </div>
</template>

<script>
// import Area from "../components/charts/area.vue"
import RadialBar from "../components/charts/radialBar.vue"
import Treemap from "../components/charts/treemap.vue"
import Column from "../components/charts/column.vue"
import Area from '../components/charts/area.vue'


export default {
    components:{

        // RadialBar,
        Treemap,
        Column,
        Area
    },
    props:
    {
        types_arr:
        {
            type:Array
        },
        json_data:{
            type:Array

        }
    },
    data(){
        return{
        }
    },

    created(){
        console.log("graph created")
        console.log(this.json_data);


    },
    watch: { 
      	json_data: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal);
          this.json_data=newVal;
        }
    }

}
</script>

<style>
#allCharts{
   margin-left: 2%; 
}
#charts1{
    margin-top: 2%;
    
    margin-bottom: 2%;
    display:flex;
}
</style>
