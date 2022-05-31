<template>
  <div id="charts">
      <!-- <Area :json_data="json_data"></Area> -->
      <Treemap :json_data="json_data"></Treemap>
      <Area :json_data="json_data"></Area>
      <Column :json_data="json_data"></Column>

  </div>
</template>

<script>
// import Area from "../components/charts/area.vue"
import RadialBar from "../components/charts/radialBar.vue"
import Treemap from "../components/charts/treemap.vue"
import Column from "../components/charts/column.vue"
import Area from './charts/area.vue'


export default {
    components:{

        // RadialBar,
        Treemap,
        Column,
        Area,
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
#charts{
    margin-top: 3%;
    margin-left: 2%;
    display:flex;
}
</style>
