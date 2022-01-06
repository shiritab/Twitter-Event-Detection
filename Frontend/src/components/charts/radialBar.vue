<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">radial bar</h3>
      <apexchart type="radialBar" :height="280" :options="options" :series="series" @click="clickHandler"></apexchart>
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
    methods: {
        clickHandler(event, chartContext, config){
            console.log("click")
            console.log(event)
            console.log(chartContext)
            console.log(config)
    },
    },
        data(){
        return{

            options : {
                chart: {
                    id: 'sessions-chart',
                },
                labels: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
                legend: {
                    position: 'bottom',
                },
            },

            series :[90,60,77,70,40,59],
          }
    }

}
</script>

<style>

</style>