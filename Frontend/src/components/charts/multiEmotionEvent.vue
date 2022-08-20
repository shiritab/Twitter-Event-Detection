<template>
  <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:100%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Average Sentiment By Event </h3>
      <apexchart ref="realTimeChart" type="bar" height="350" :options="options" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: "MultiEmotionEvent",
    components:{
        apexchart: VueApexCharts,
        
    },
    props:{
        json_data:{type:Array}
    },
    methods:{
        make_data(){
            /** Build data for graph */
            this.list_data = [];

            // calculate average sentiment for each event
            this.json_data.forEach((event)=>{
                const average = this.average(event.tweets_emotion) * 100;
                var dict={name:event.event,data: [average]};
                this.list_data.push(dict);
            })
            this.series=this.list_data;
        },

        average(array){
            return array.reduce((a,b) => a + b, 0) / array.length
        }
    },
    created(){
        console.log("created emotionChart")
        this.make_data()
    },
    data() {
        return{ 
            list_data: [],
            series: [],
            options: {
                plotOptions: {
                    bar: {
                        colors: {
                            ranges: [
                                {
                                    from: -100,
                                    to: -30,
                                    color: '#f13636'
                                },
                                {
                                    from: -30,
                                    to: -10,
                                    color: '#F15B46'
                                }, 
                                {
                                    from: -10,
                                    to: 0,
                                    color: '#FEB019'
                                },
                                {
                                    from: 0,
                                    to: 10,
                                    color: 'rgb(15, 165, 224)'
                                },
                                {
                                    from: 10,
                                    to: 30,
                                    color: 'rgb(17, 134, 180)'
                                },
                                {
                                    from: 30,
                                    to: 100,
                                    color: 'rgb(12, 107, 145)'
                                }
                            ]
                        },
                        columnWidth: '100%',
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
                        "Events"
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
        }
    },
    // computed: {
    //     changeOptions: function() {
    //         return null;
    //     }
    // }

}
</script>

<style>

</style>