<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">area</h3>
      <apexchart type="area" :height="280" :options="options" :series="series"></apexchart>
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
  
            categories: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
            options : {
            chart: {
                id: 'pageview-chart',
                toolbar: {
                show: false,
                },
                
            events: {
                click(event, chartContext, config) {
                    console.log(this.categories);
                    console.log(config.dataPointIndex);
                    change(config.dataPointIndex)
            }
            }
            },
            dataLabels: {
                enabled: false,
            },
            xaxis: {
                categories: this.categories,
            },
            },

            series : [
            {
                data: [0.8, 0.59, 0.7, 0.7, 0.3, 0.9],
            },
            ],}
},
methods:{
    change(num){
        console.log(num);
    }
}
  
  

}
</script>

<style>

</style>