<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">treemap</h3>
      <apexchart type="treemap" :height="280" :options="options" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    components:{
        apexchart: VueApexCharts,
        
    },
    props:{
        data:{type:Object}
    },
    data(){
        return{
            
        series: [
            {
              data: [
                {
                  x: 'event 1',
                  y: 218
                },
                {
                  x: 'event 2',
                  y: 149
                },
                {
                  x: 'event 3',
                  y: 184
                },
                {
                  x: 'event 4',
                  y: 55
                },
                {
                  x: 'event 5',
                  y: 84
                },
                {
                  x: 'event 6',
                  y: 43
                }, 
              ]
            }
          ],
          options: {
            plotOptions: {
              treemap: {
                distributed: true,
               
              }
            }
          },
  

}
    }
}
</script>

<style>

</style>