<template>
  <div id="home-page">
      <h1> Trending </h1>
      <br>
      <!-- a select button for algorithm picker -->
      <b-form-select style="width:20%" v-model="selected" :options="['SEDTWik', 'twembeddings', 'algorithm 3','algorithm 4']"></b-form-select>
      <!-- <Card :infos=infos></Card> -->
      <div id="charts">
      <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">chart1</h3>
      <apexchart type="area" :height="280" :options="pageViewOptions" :series="pageViewSeries"></apexchart>
    </div>

    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">chart2</h3>
      <apexchart type="radialBar" :height="280" :options="sessionsOptions" :series="sessionsSeries"></apexchart>
    </div>

    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4">chart3</h3>
                <apexchart type="treemap" :height="280" :options="chartOptions" :series="series"></apexchart>

    </div>
      </div>
  </div>
</template>

<script>
// import Card from "./../components/Card.vue"
import VueApexCharts from 'vue-apexcharts'
export default {
    name: "HomePage",
    components:{
        apexchart: VueApexCharts,
        // Card,
    },
    props: {
        algorithms:{
            type: Array,
            required: true
        }
    },
    data(){
        return{
            selected: null,
            infos: [
                {
                    title: "bla",
                },
                {
                    title: "bla2"
                },
                {
                    title: "bla3"
                }
            ],


            pageViewOptions : {
            chart: {
                id: 'pageview-chart',
                toolbar: {
                show: false,
                },
            },
            dataLabels: {
                enabled: false,
            },
            xaxis: {
                categories: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
            },
            },

            pageViewSeries : [
            {
                data: [0.8, 0.59, 0.7, 0.7, 0.3, 0.9],
            },
            ],


            sessionsOptions : {
                chart: {
                    id: 'sessions-chart',
                },
                labels: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
                legend: {
                    position: 'bottom',
                },
            },

            sessionsSeries :[90,60,77,70,40,59],

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
          chartOptions: {
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
#home-page{
    text-align: center;
}
#charts{
    margin-top: 3%;
    margin-left: 2%;
    display:flex;
}
</style>