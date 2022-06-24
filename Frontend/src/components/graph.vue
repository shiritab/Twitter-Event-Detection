<template>
  <div id="allCharts">
      <div id="charts1">
        <Treemap :json_data="algorithm_results"></Treemap>
        <HomeEventsAmountByDate :json_data="algorithm_results"></HomeEventsAmountByDate>
      </div>
      <MultiEventEmotion :json_data="algorithm_results"></MultiEventEmotion>

  </div>
</template>

<script>
import Treemap from "../components/charts/treemap.vue"
import MultiEventEmotion from "./charts/multiEventEmotion.vue"
import HomeEventsAmountByDate from './charts/homeEventsAmountByDate.vue'


export default {
    components:{

        Treemap,
        MultiEventEmotion,
        HomeEventsAmountByDate
    },
    props:
    {
        types_arr:
        {
            type:Array
        },
        algorithm_results:{
            type:Array

        }
    },
    data(){
        return{
        }
    },

    created(){
        console.log("graph created")
        console.log(this.algorithm_results);


    },
    watch: { 
      	algorithm_results: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal);
          this.algorithm_results = newVal;
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
