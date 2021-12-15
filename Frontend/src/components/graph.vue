<template>
  <div id="charts">
      <Area :json_data="json_data"></Area>
      <RadialBar :json_data="json_data"></RadialBar>
      <Treemap :json_data="json_data"></Treemap>


  </div>
</template>

<script>
import Area from "../components/charts/area.vue"
import RadialBar from "../components/charts/radialBar.vue"
import Treemap from "../components/charts/treemap.vue"


export default {
    components:{
        Area,
        RadialBar,
        Treemap
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
        console.log("graph mounted")
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
