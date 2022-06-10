<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:50%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Event Relative Traffic</h3>
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
                test:"checkkkkkkk",
          list_data:[],
          series: [
              {
                data: []
              }
            ],
          // options: {
          //   plotOptions: {
              
          //     treemap: {
          //       distributed: true,
               
          //     },

          //   },
          //   chart:{
          //     type:"treemap",
          //     events: {

          //       click: function(event, chartContext, config) {
                  
          //           var index=0;
                    
          //           console.log(config.dataPointIndex);
          //           change()
          //   },

          //   }}
          
            
          // },
          
}},
    methods:{

      change: function(index){
        console.log("change")
      },
      handle(){
        console.log("heyyy");
        return "hellppppp"
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
      // localStorage.setItem("router",JSON.stringify(this.$router))
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
    computed:{

                options: function(){
                  return{
            plotOptions: {
              
              treemap: {
                distributed: true,
               
              },

            },
            chart:{
              type:"treemap",
              events: {

                click: function(event, chartContext, config) {
                  
                    var index=0;
                    console.log(chartContext);
                    console.log(config);
                    console.log(config.dataPointIndex);
                    const data=JSON.parse(localStorage.getItem("data_algorithm"))
                    console.log(data[config.dataPointIndex]);
                    
                    // const router=JSON.parse(localStorage.getItem("router"));
                    // console.log(router);
                    // router.push({ name: 'event', params: {id:data[config.dataPointIndex].event, tweets:data[config.dataPointIndex].tweets}});
                   
            },

            }}
          
            
          }
                }
    },

    

    
}
</script>

<style>

</style>