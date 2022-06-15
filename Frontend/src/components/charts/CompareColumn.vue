<template>
  <div id="chart" class="compareCol">
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:90%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Algorithms Performance</h3>
      <apexchart type="bar" height="350" :options="chartOptions" :series="get_score"></apexchart>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: 'CompareColumn',
    components:{
        apexchart: VueApexCharts,
    },
    props:{
      algorithms:{
        type:Array
      }
    },
    data(){
        return{
          json_return:[{
                name: 'SedTwik',
                data: [0.84,0.79]//, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'Twembeddings',
                data: [0.6,0.89]//, 98, 87, 105, 91, 114, 94]
            }, {
                name: 'Bert',
                data: [0.77,0.55]//, 26, 45, 48, 52, 53, 41]
            }],
            series: [{
                name: 'SedTwik',
                data: [0.84,0.79]//, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'Twembeddings',
                data: [0.6,0.89]//, 98, 87, 105, 91, 114, 94]
            }, {
                name: 'Bert',
                data: [0.77,0.55]//, 26, 45, 48, 52, 53, 41]
            }],
            
            chartOptions: { 
                chart: {
              type: 'bar',
              height: 350
            },
            plotOptions: {
              bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'
              },
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              show: true,
              width: 2,
              colors: ['transparent']
            },
            xaxis: {
              categories: ["Normalized Mutual Info"," Adjusted Rand"], //, 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },

            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return  val*100 +" %"
                }
              }
            }
            }
        }
    },

    computed:{
      get_score(){
        var new_list=[]
        this.json_return.map(dict=>{
            if (this.algorithms.includes(dict.name)){
              new_list.push(dict);
            }
        });
        // console.log(this.json_return)
        // console.log(new_list);
        return new_list
      }
    },
   async mounted(){
      try{
          const compare_score = await this.axios.get(`${this.$root.serverLink}/algorithm/compare`);
          this.json_return = compare_score.data;
          this.series=this.json_return;
          console.log(this.series);

      } catch(error){  
          console.log(`error ${error}\noccured at compare algorithms`);
      }
    }
    
}
</script>

<style>
.compareCol{
    width: 50%;
    margin-left: 4%;
}
</style>