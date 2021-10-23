<template>
  <div id="charts">
      <Area :data="data"></Area>
      <RadialBar :data="data"></RadialBar>
      <Treemap :data="data"></Treemap>


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
        }
    },
    data(){
        return{
            data:new Object
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
