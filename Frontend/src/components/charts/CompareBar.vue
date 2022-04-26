<template>
  <div id="chart" class="compareBar">
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:95%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Num of events</h3>
      <apexchart type="bar" height="300" :options="chartOptions" :series="series"></apexchart>
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
            data: [6,2350,1189]
          }],
          chartOptions: {
            chart: {
              type: 'bar',
              height: 200
            },
            plotOptions: {
              bar: {
                barHeight: '100%',
                distributed: true,
                horizontal: true,
                dataLabels: {
                  position: 'bottom'
                },
              }
            },
            colors: ['#69d2e7', '#f9a3a4', '#2b908f'
            ],
            dataLabels: {
              enabled: true,
              textAnchor: 'start',
              style: {
                colors: ['black']
                
              },
              formatter: function (val, opt) {
                return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
              },
              offsetX: 0,

            },
            stroke: {
              width: 1,
              colors: ['#fff']
            },
            xaxis: {
              categories: ['Sedwix','Twembeddings','Bert topic'
              ],
            },
            yaxis: {
              labels: {
                show: false
              }
            },

            tooltip: {
              theme: 'dark',
              x: {
                show: false
              },
              y: {
                title: {
                  formatter: function () {
                    return ''
                  }
                }
              }
            }
          },
            
        }
    }
}
</script>

<style>
.compareBar{
    width: 40%;
}
</style>