<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:50%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Event Size</h3>
      <apexchart ref="realtimeChart" type="treemap" :height="280"  :options="options" :series="series" ></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    components:{
        apexchart: VueApexCharts,
        
    },
    props:{
        json_data:{type:Array}
    },

    data(){
        return{
          list_data:[],
          series: [
              {
                data: []
              }
          ],
          options: {
            plotOptions: {
              
              treemap: {
                distributed: true,
               
              }
            },}
}},
    methods:{
      make_data(){
        /** Build data for graph */
        this.list_data = [];

        // calculate number of tweets for each event
        this.json_data.forEach((event)=>{
          var dict={x:event.event,y:event.tweets.length};
          this.list_data.push(dict);
        
        })
        this.series[0].data=this.list_data;
        this.data=this.list_data;

      },
      change: function(index){
        console.log("change")
      },
    },
    created (){
      console.log("created treemap");
      this.make_data();

    }, 
    watch: { 
      json_data: function(newVal, oldVal) { // watch it
        console.log('Prop changed: ', newVal, ' | was: ', oldVal)
        this.json_data=newVal
        this.make_data();
        
        this.$refs.realtimeChart.updateSeries(
          [
            {
              data: this.series[0].data,
            }
          ],
          false, 
          true
        );
        console.log(this.series);
      }
    },
   
}
</script>

<style>

</style>