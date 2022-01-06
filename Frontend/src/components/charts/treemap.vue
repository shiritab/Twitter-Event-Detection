<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Event relative traffic</h3>
      <apexchart ref="realtimeChart" type="treemap" :height="280" :options="options" :series="series" @click="change"></apexchart>
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
    methods:{
      change(){
        console.log("hello")
      },
      make_data(){
        console.log("make_data");
        this.list_data = [];
        this.json_data.forEach((event)=>{
          var dict={x:event.event,y:event.tweets.length};
          this.list_data.push(dict);
        
        })
        console.log(this.list_data);
        this.series[0].data=this.list_data;
      }
    },
    created (){
      console.log(this.json_data);
      this.make_data();

      console.log(this.series);

    },
    watch: { 
      	json_data: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)
          this.json_data=newVal
          this.make_data();
          
      this.$refs.realtimeChart.updateSeries([{
        data: this.series[0].data,
      }], false, true);
    


        }
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
            },
            
              events: {
                click(event, chartContext, config) {
                    console.log(this.categories);
                    console.log(config.dataPointIndex);
            }
            }
          
            
          },
          
}

    }
}
</script>

<style>

</style>