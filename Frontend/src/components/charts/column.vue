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
        },
        average(array){
            return array.reduce((a,b) => a + b, 0) / array.length
        }
    },
    data() {
        return{ 
            list_data: [],
            series: [],
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
                    categories: [
                        '2012-10-12'
                        // '2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01', '2011-05-01', '2011-06-01',
                        // '2011-07-01', '2011-08-01', '2011-09-01', '2011-10-01', '2011-11-01', '2011-12-01',
                        // '2012-01-01', '2012-02-01', '2012-03-01', '2012-04-01', '2012-05-01', '2012-06-01',
                        // '2012-07-01', '2012-08-01', '2012-09-01', '2012-10-01', '2012-11-01', '2012-12-01',
                        // '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01', '2013-05-01', '2013-06-01',
                        // '2013-07-01', '2013-08-01', '2013-09-01'
                    ],
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
    computed: {
        changeOptions: function() {
            return null;
        }
    }

}
</script>

<style>

</style>