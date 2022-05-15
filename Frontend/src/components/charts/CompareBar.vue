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
    props:{
      algorithms:{
        type:Array
      }
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
              categories: ['Sedwix','Twembeddings','Bert topic'],
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
        console.log(this.algorithms);
        var new_list=[]
        this.json_return.map(dict=>{
            if (this.algorithms.includes(dict.name)){
              new_list.push(dict);
            }
        });
        console.log(this.json_return)
        console.log(new_list);
        return new_list
      }
    },
      //  async mounted(){
  //     try{
  //               const compare_score = await this.axios.get(`http://127.0.0.1:5000/algorithm/compare`);
  //               this.json_return = compare_score.data;
  //               this.series=this.json_return;
  //           } catch(error){
                
  //               console.log(`error ${error}\noccured at getEventsSummary on HomePage.vue`);
  //           }
  //   }
}
</script>

<style>
.compareBar{
    width: 40%;
}
</style>