<template>
  <div id="chart" class="compareBar">
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:95%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Number of Events</h3>
      <apexchart type="bar" height="300" :options="get_category" :series="get_score"></apexchart>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: 'CompareAlgorithmEventAmount',
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
          algorithm_event_amount_dict:{"SedTwik":52,'Twembeddings':100,'Bert':40},
        series: [{
            data: [52,100,100]
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
              categories: ['SedTwik','Twembeddings','Bert'],
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
    },
    computed:{
    get_score(){
        /** Sets events' amount of each algorithm */

        var algorithm_events_amount_list=[];
        var categories_list=[];
        for(var key in this.algorithm_event_amount_dict) {
            if (this.algorithms.includes(key)){
              algorithm_events_amount_list.push(this.algorithm_event_amount_dict[key]);
              categories_list.push(key);
            }
        }

        return [{data: algorithm_events_amount_list}]
      },
      get_category(){
        /** Get algorithms as categories */
        
        var option=this.chartOptions;
        var categories_list=[];
        for(var key in this.algorithm_event_amount_dict) {
            if (this.algorithms.includes(key)){
              categories_list.push(key);
            }
        }
        option.xaxis={categories: categories_list};
        console.log(option);
        return option;
      }
    },
}
</script>

<style>
.compareBar{
    width: 40%;
}
</style>