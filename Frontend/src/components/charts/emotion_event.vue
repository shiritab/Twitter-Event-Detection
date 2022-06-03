<template>
  <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:5 0%; margin-right:3%">
      <h3 class="text-xl text-gray-600 mb-4" >Event's average emotion positivity by date</h3>
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
        emotion:{type:Array},
        dates:{type:Array}
    },
    methods:{
        make_data(){
            console.log("create emotion chart")
            var date_dict={}
            var date_list=[]
            console.log(this.emotion);
            console.log(this.dates);
            for (let i = 0; i < this.dates.length; i++) {
                if (this.dates[i] in date_dict){
                    date_dict[this.dates[i]].push(this.emotion[i]);
                }
                else{
                    date_list.push(this.dates[i]);
                    date_dict[this.dates[i]]=[this.emotion[i]];
                }
            }
            console.log(date_dict);
           var sort_date=date_list.sort()
            var data_list=[];
            console.log(sort_date);
            sort_date.forEach((date)=>{
                console.log(date);
                const average = this.average(date_dict[date]) * 100;
                var dict={name:date,data: [average]};
                this.list_data.push(dict);
            })
            
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
                        "Dates"
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
    created(){
        this.make_data()
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