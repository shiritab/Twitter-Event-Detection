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
          data_dict:{"SedTwik":52,'Twembeddings':100,'Bert':40},
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

        var data_list=[];
        var categories_list=[];
        for(var key in this.data_dict) {
            if (this.algorithms.includes(key)){
              data_list.push(this.data_dict[key]);
              categories_list.push(key);
            }
        }

        return [{data: data_list}]
      },
      get_category(){
        var option=this.chartOptions;
        var categories_list=[];
        for(var key in this.data_dict) {
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