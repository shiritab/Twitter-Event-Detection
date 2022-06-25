<template>
  <div id="allCharts">
      <div id="charts1">
      <Treemap :json_data="json_data"></Treemap>
      <EventsAmountByDate :json_data="json_data"></EventsAmountByDate>
      </div>
      <MultiEmotionEvent :json_data="json_data"></MultiEmotionEvent>

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
        json_data:{
            type:Array

        }
    },
    data(){
        return{
        }
    },
    watch: { 
      	json_data: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal);
          this.json_data=newVal;
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
