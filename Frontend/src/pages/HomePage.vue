<template>
  <div id="home-page">
    <h1> Trending </h1>
    <div class="run-data">
        <div class="row">
            <div class="col-4">
                <a>Dataset:</a>
                <br>
                    <b-form-select style="width:100%; margin-left:2%" v-model="dataset" :options="dataset_option"></b-form-select>

            </div>
            <div class="col-4">
                <a>Algorithm:</a>
                <br>
                <b-form-select style="width:100%" v-model="algorithm" :options="this.algorithms"></b-form-select>
            </div>
            <div class="col-4">

                <input type="file" id="uploadmyfile"  ref="file" @change="requestUploadFile" style="display: none">
                <b-button style="margin-top:1%; width:100%" class="upload-button" variant="info" @click="$refs.file.click()">
                    <b-icon icon="cloud-arrow-up" aria-hidden="true"></b-icon>
                        Upload Data 
                </b-button>

                <b-button  style="margin-top:1%; width:100%"  class="upload-button" variant="info" @click="getEventSummary()">
                    <b-icon icon="play" aria-hidden="true"></b-icon> Run
                </b-button>
            </div>
        </div>
    </div>


    <div class="grid grid-cols-1 gap-4 px-4 mt-8 sm:grid-cols-4 sm:px-8" id="info">

        <!-- Total tweets -->
        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-chat-left-text-fill" viewBox="0 0 16 16">
                    <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4.414a1 1 0 0 0-.707.293L.854 15.146A.5.5 0 0 1 0 14.793V2zm3.5 1a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5z"/>
                </svg>
            </div>

            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Total Tweets</h3>
                <p class="text-3xl">{{total_tweets}}</p>
            </div>
        </div>

         <!-- Dates range -->        
        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-calendar-date-fill" viewBox="0 0 16 16">
                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zm9.954 3H2.545c-.3 0-.545.224-.545.5v1c0 .276.244.5.545.5h10.91c.3 0 .545-.224.545-.5v-1c0-.276-.244-.5-.546-.5zM8.5 7a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm3 0a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zM3 10.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z"/>
                </svg>
            </div>

            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Dates Range</h3>
                <p class="text-3xl">{{dates_range}}</p>
            </div>
        </div>

        <!-- Total events -->
        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg width="50" height="50" fill="currentColor" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M13,9.5H18V7.5H13V9.5M13,16.5H18V14.5H13V16.5M19,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H19A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21M6,11H11V6H6V11M7,7H10V10H7V7M6,18H11V13H6V18M7,14H10V17H7V14Z" />
                </svg>
            </div>

            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Total Events</h3>
                <p class="text-3xl">{{algorithm_results.length}}</p>
            </div>
        </div>
    </div>

                
    <Graph :v-if="created" :algorithm_results="algorithm_results"></Graph>
    <br>
<br>
        <h3>Detected Events</h3>
        <b-table fixed striped hover 
        :items="algorithm_results" 
        :fields="fields_tweets_info"
        :sort-by="sort_events_by"
        :sort-compare="sortEventsCompare">
            <template #cell(num_of_tweets)="data">
                {{data.item.tweets.length}}
            </template>
            <template #cell(event_date)="data">
                {{data.item.dates.length > 0 ? data.item.dates[0]: " - "}}
            </template>
            <template #cell(event)="data">
                <router-link :to="{ name: 'event', params: {name:data.item.event, tweets:data.item.tweets,dates:data.item.dates,emotion:data.item.tweets_emotion}}">
                    {{data.item.event}}
                </router-link>
            </template>
        </b-table>
    
    <b-toast id="non-selected-algorithm-toast" variant="info" solid>
      <template #toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">INFO</strong>
        </div>
      </template>
      Please choose to run a valid algorithm.
    </b-toast>

  </div>
</template>

<script>
import axios from "axios";

import Graph from "../components/graph.vue"
export default {
    name: "HomePage",
    components:{
        Graph 
    },
    data(){
        return{
            created:false,
            dataset_option: ["event2012.json"],
            algorithm: null,
            algorithms: [
                {value: null, text: "Select algorithm"}
            ],
            dataset: "event2012.json",
            selected_file: "",
            src: "",
            file: "",
            total_autors:0,
            total_tweets:0,
            total_events:0,
            algorithm_results:[],
            fields_tweets_info:[
                {key: 'event', sortable: true },
                {key: 'event_date', sortable: true },
                {key: 'num_of_tweets', sortable: true }
            ],
            sort_events_by: 'num_of_tweets'
        }
    },
    methods: {

        myRowClickHandler(record, index) {
            console.log(record); 
            this.$router.push({ name: 'event', params: 1 });
        },

        async getEventSummary(){
            /* Get request for running chosen algorithm and receive it's summarized results */
            
            if (this.algorithm == null) {
                this.$bvToast.show('non-selected-algorithm-toast');
                return;
            }

            localStorage.setItem('algorithm',this.algorithm);
            localStorage.setItem('chosen_dataset', this.dataset);
            try{
                console.log(`selected: ${this.selected_file}`);
                
                // run algorithm
                const events = await this.axios.get(`${this.$root.serverLink}/algorithm/${this.algorithm}?dataset=${this.dataset}`);
                
                // get events
                const event = await this.axios.get(`${this.$root.serverLink}/events/summary/${this.algorithm}`);

                this.algorithm_results = event.data;
            } catch(error){
                this.algorithm_results=require("../../../Backend/results/sedtwik/summarized_event2012.json");
                console.log(`error ${error}\noccured at getEventsSummary on HomePage.vue`);
            }

            //  add here the trim function
            this.algorithm_results.map((res) =>{
                res.event = res.event.trim();
                return res;
            })
            this.total_events = this.algorithm_results.length;
            this.total_tweets = this.algorithm_results.reduce((total, event) => {
                return total + event.tweets.length;
            }, 0)
            this.dates_range = this.getEventsDates();
            localStorage.setItem('data_algorithm',JSON.stringify(this.algorithm_results));
            localStorage.setItem("total_events", this.total_events);
            localStorage.setItem("total_tweets", this.total_tweets);
            localStorage.setItem("dates_range", this.dates_range);
            localStorage.setItem("router", this.$router);
        },
        getEventsDates(){
            /* Computes and returns dates range (min date, max date) in algorithm's results */
            var minDate="";
            var maxDate="";

            let all_dates_set = [];
            this.algorithm_results.map((event) => {
                 all_dates_set = all_dates_set.concat(event.dates_set);
            });

            const all_dates_set_sorted = all_dates_set.sort();
            minDate = all_dates_set_sorted[0];
            maxDate = all_dates_set_sorted[all_dates_set_sorted.length -1];

            return `${minDate.replace('-',"/").replace('-',"/")} - ${maxDate.replace('-',"/").replace('-',"/")}`;
            
        },

        requestUploadFile(args){
            /* Post request to save uploaded file to server side */
            this.file = this.$refs.file.files[0];
            this.src=this.file.name
            this.dataset_option.push(this.src)
            const formData = new FormData();
            formData.append('file', this.file);
            const headers = { 'Content-Type': 'application/json' };
            
            axios.post(`${this.$root.serverLink}/files/upload`, formData, { headers }).then((res) => {
                //   res.data.files; // binary representation of the file
                res.status; // HTTP status
            });
            console.log(this.file)
        },
        
        async getAlgorithms() {
            /* Get request for all saved algorithms */

            try {
                const algorithms = await this.axios.get(`${this.$root.serverLink}/algorithm/all`);
           
                algorithms.data.map((algorithm) => {
                    this.algorithms.push(algorithm);
                });
            } catch (error) {
                const default_algorithms = ['SedTwik', 'Twembeddings', 'Bert'];
                default_algorithms.map((algorithm) => {
                    this.algorithms.push(algorithm);
                });
                console.log(`error occured on getAlgorithms HomePage. error: ${error}`);
            }
        },

        getLastRun() {
            /* If local storage contains past execution result, sets past results to variables and returns true,
             otherwise false */

            const algorithm = localStorage.getItem("algorithm");
            const data_algorithm = localStorage.getItem("data_algorithm");
            
            if (algorithm && data_algorithm) {
                this.algorithm = algorithm;
                this.algorithm_results = JSON.parse(data_algorithm);
                this.total_events = localStorage.getItem("total_events");
                this.total_tweets = localStorage.getItem("total_tweets");
                this.dates_range = localStorage.getItem("dates_range"); 
                return true;
            }
            return false;
        },
        sortEventsCompare(row1, row2, key) {
            /**
             * Given two different rows and a column key, we compare them by substracting.
             * if key is not event_date nor num_of_tweets, we compare by default.
             */
            if (key === 'event_date') {
                return this.dateFormat(row1.dates[0]) - this.dateFormat(row2.dates[0]);
            } else if (key === 'num_of_tweets') {
                return row1.tweets.length - row2.tweets.length;
            } else {
                // Let b-table handle sorting other fields (other than `date` field)
                return false;
            }
        },
        dateFormat(dateString) {
            /*
            Given a string of the format "yyyy-mm-dd" we return a Date object.
            notice: if date isn't valid we return current date.
            */
            const dateSplit = dateString.split("-");
            let dateFormatted;
            if (dateSplit.length == 3) {
                dateFormatted = new Date(dateSplit[0], dateSplit[1], dateSplit[2]);
            } else {
                dateFormatted = new Date();
            }
            return dateFormatted;
        }
    },

    created(){
        
        console.log("HomePage created");
        this.getAlgorithms();

        // if there is not previous results
        if (!this.getLastRun()) {
            this.getEventSummary();
            localStorage.setItem('algorithm', this.algorithm);
        }
        
        this.created=true;
    },


    
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans&family=Merienda:wght@700&display=swap');

#charts{
    margin-top: 3%;
    margin-left: 2%;
    display:flex;
}
.grid{
    display: flex;
}
#icon{
    display: flex;
    margin-left: 10px;
}
.table{
    overflow-x: scroll;
    overflow-y:scroll;
    margin: auto;
    height: 300px;


}
.b-table{
    background-color: white;
    opacity: 8.0;

}
.mb-2{
    float: left;
    margin-left: 2%;
}

.upload-file{
    background-color: aqua;
}
.run-data{
background-color: rgb(218, 217, 217);
  padding: 10px;
  width: 50%;
  margin-bottom: 10px;
  margin-left: 25%;
  align-items: center;
  text-align: center;
  border-radius: 10px;
  opacity: 8.0;
}

#info{
    display: inline-flex;
}
</style>
