<template>
  <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:30%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Event's average emotion positivity</h3>
      <apexchart ref="realTimeChart" type="bar" height="350" :options="options" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: "Column",
    components:{
        apexchart: VueApexCharts,
        
    },
    props:{
        json_data:{type:Array}
    },
    methods:{
        make_data(){
            console.log("make_data column");
            console.log(this.json_data)
            this.list_data = [];
            this.json_data.forEach((event)=>{
                const average = this.average(event.tweets_emotion) * 100;
                var dict={name:event.event,data: [average]};
                this.list_data.push(dict);
            })
            // console.log(this.list_data);
            this.series=this.list_data;
            this.series=[1,2,3,4,5,6];
        },
        average(array){
            return array.reduce((a,b) => a + b, 0) / array.length
        }
    },
    data() {
        return{ 
            list_data: [],
            series:[1,2,3,4,5,6],
            options: {
                plotOptions: {
                    bar: {
                        colors: {
                            ranges: [{
                                from: -100,
                                to: -46,
                                color: '#F15B46'
                            }, {
                                from: -45,
                                to: 0,
                                color: '#FEB019'
                            }]
                        },
                        columnWidth: '80%',
                    }
                },
                dataLabels: {
                    enabled: false,
                },
                yaxis: {
                    title: {
                        text: 'Emotion value',
                    },
                    labels: {
                        formatter: function (y) {
                        return y.toFixed(0) + "%";
                        }
                    }
                },
                xaxis: {
                    type: 'date',
                    categories: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
                    labels: {
                        rotate: -90
                    }
                },
            },
        }
    },
    watch: { 
      	json_data: function(newVal, oldVal) { // watch it
          console.log('Prop changed on column: ', newVal, ' | was: ', oldVal)
          this.json_data=newVal
          this.make_data();
          
      this.$refs.realtimeChart.updateSeries([{
        data: this.series,
      }], false, true);
    


        }
    },

}
</script>

<style>

</style>