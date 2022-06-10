<template>
    <div class="px-4 py-2 bg-white border rounded-md overflow-hidden shadow" style="width:50%; margin-right:2%">
      <h3 class="text-xl text-gray-600 mb-4">Events Amount By Date</h3>
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
        json_data:{type :Array}
    },
    data(){
        return{
  
            categories: ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6'],
            options : {
                colors:["#8af136"],
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

    make_data(){
        console.log("make_data");
        var date_dict={};
        var date_list=[];
        this.json_data.forEach((event)=>{
            event.dates_set.forEach((date)=>{
                if (date in date_dict){
                    date_dict[date]+=1;
                }
                else{
                    date_list.push(date);
                    date_dict[date]=1;
                }
            })
        })
        // sort(date_dict);
        console.log("this is area dict");
        console.log(date_dict);
        //series =[{data:[1,1,1,1,1,1,1]}]
        var sort_date=date_list.sort()
        var data_list=[];
        sort_date.forEach((date)=>{
            data_list.push(date_dict[date]);
        })
        this.series=[{data:data_list}];
        this.categories=sort_date;
        console.log(this.categories);
        this.options.xaxis={categories:sort_date}


      }
    },
      watch: { 
      	json_data: function(newVal, oldVal) { // watch it
            console.log('Prop changed on column: ', newVal, ' | was: ', oldVal)
            this.json_data=newVal
            this.make_data();
 
        }
    },
    computed: {
        changeOptions: function() {
            return null;
        }
    },
    created (){
        console.log("this is area chart!!!!!")
      this.make_data();


    },
}
  
  


</script>

<style>

</style>