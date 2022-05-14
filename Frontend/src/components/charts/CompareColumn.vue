<template>
  <div id="chart" class="compareCol">
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:95%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Algorithms performance</h3>
      <apexchart type="bar" height="350" :options="chartOptions" :series="series"></apexchart>
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
    data(){
        return{
            series: [{
                name: 'Sedwik',
                data: [0.84,0.79,0.5]//, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'Twembeddings',
                data: [0.6,0.89,0.48]//, 98, 87, 105, 91, 114, 94]
            }, {
                name: 'Bert Topic',
                data: [0.77,0.55,0.69]//, 26, 45, 48, 52, 53, 41]
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
              categories: ['Precision', 'Recall', 'F1-Score'], //, 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },

            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return "$ " + val + " thousands"
                }
              }
            }
            }
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