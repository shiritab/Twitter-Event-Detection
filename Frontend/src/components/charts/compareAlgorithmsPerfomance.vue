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
    name: 'CompareAlgorithmsPerfomance',
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
            algorithm_measure_performance: [],
            series: [],
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
              categories: ["Normalized Mutual Info"," Adjusted Rand"],
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
        /** Get score of each algorithm */

        var new_list=[]
        this.algorithm_measure_performance.map(dict=>{
            if (this.algorithms.includes(dict.name)){
              new_list.push(dict);
            }
        });
        return new_list
      }
    },
   async mounted(){
      try{
          const compare_score = await this.axios.get(`${this.$root.serverLink}/algorithm/compare`);
          this.algorithm_measure_performance = compare_score.data;
          this.series=this.algorithm_measure_performance;
          console.log(this.series);

      } catch(error){  
          this.algorithm_measure_performance = [{
                name: 'SedTwik',
                data: [0.84,0.79]
            }, {
                name: 'Twembeddings',
                data: [0.6,0.89]
            }, {
                name: 'Bert',
                data: [0.77,0.55]
            }];
          this.series = this.algorithm_measure_performance;
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