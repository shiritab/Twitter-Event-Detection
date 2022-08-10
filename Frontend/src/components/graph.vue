<template>
  <div id="allCharts">
      <div id="charts1">
      <Treemap :json_data="algorithm_results"></Treemap>
      <EventsAmountByDate :json_data="algorithm_results"></EventsAmountByDate>
      </div>
      <MultiEmotionEvent :json_data="algorithm_results"></MultiEmotionEvent>

  </div>
</template>

<script>
import Treemap from "../components/charts/treemap.vue"
import MultiEmotionEvent from "../components/charts/multiEmotionEvent.vue"
import EventsAmountByDate from '../components/charts/eventsAmountByDate.vue'


export default {
    components:{
        Treemap,
        MultiEmotionEvent,
        EventsAmountByDate
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
    watch: { 
      	algorithm_results: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal);
          this.algorithm_results = newVal;
        }
    },
    created(){
        console.log("graph created")
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
