<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:48%; margin-right:2%, height:180px">
      <h3 class="text-xl text-gray-600 mb-4" style="font-size:22px">Tweets Count By Date</h3>
      <apexchart type="area" :height="180" :options="options" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
    name: "TweetsAmountByDate",
    components:{
        apexchart: VueApexCharts,
        
    },
    props:{
        dates:{type :Array}
    },
    data(){
        return{
            categories: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
            options : {
                colors:["#f13693"],  
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
            ],
        }
    },
    methods:{
        make_data(){
            /** Build xaxis and yaxis for graph */
            var date_dict={};
            var date_list=[];

            // calculate number of tweets occured on each date
            this.dates.forEach((date)=>{
                if (date in date_dict){
                    date_dict[date]+=1;
                }
                else{
                    date_list.push(date);
                    date_dict[date]=1;
                }
            })

            var data_list=[];
            var sort_date=date_list.sort()
            sort_date.forEach((date)=>{
                data_list.push(date_dict[date]);
            })

            this.series=[{data:data_list}];
            this.categories=sort_date;
            this.options.xaxis={categories:sort_date}
        }
    },
      watch: { 
      	dates: function(newVal, oldVal) { // watch it
            console.log('Prop changed on column: ', newVal, ' | was: ', oldVal)
            this.dates=newVal
            this.make_data();
 
        }
    },
    computed: {
        changeOptions: function() {
            return null;
        }
    },
    created (){
        console.log("created TweetsAmountByDate")
        this.make_data();
    },
}
</script>

<style>

</style>