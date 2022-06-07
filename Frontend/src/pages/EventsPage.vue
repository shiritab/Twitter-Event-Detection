<template id="Events-By-Date-Page">
  <div>
    <!-- <h1> Trending </h1> -->
    <br>
    <p>Events by algorithm: {{this.algorithm}}</p>
    <b-form-datepicker ref="datepicker"
    v-model="dateValue"
    :min="min"
    :max="max"
    @input="getEventsByDate()"
    style="width: 18.3rem; margin: auto"
    locale="en"></b-form-datepicker>
    <br>
    <!-- <b-card-group style="display:block" class="events"> -->
        <!-- <b-card v-for="event in eventsByValue"
            :key="event.id"
            style="max-width: 20rem; margin: auto;"
            bg-variant="light" class="text-center">
            <router-link :to="{ name: 'event', params:{id:event.id}}">
                <b-card-text>{{ event.name  }}</b-card-text>
            </router-link>
        </b-card> -->
        <div class="row">
        <b-card v-for="event in events"
            :key="event.event"
            style="max-width: 20rem; margin: auto;"
            bg-variant="light" class="text-center">
            <router-link :to="{ name: 'event', params:{name:event.event, tweets:event.tweets,dates:event.dates,emotion:event.tweets_emotion}}">
                <b-card-text>{{ event.event  }}</b-card-text>
            </router-link>
        </b-card>
        </div>
    <!-- </b-card-group> -->
  </div>
</template>

<script>
export default {
    name: "EventsPage",
    data() {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      // 1st two months prior
      const minDate = new Date(today);
      minDate.setYear(minDate.getYear() - 20);
      minDate.setDate(1);

      const maxDate = new Date(today)

      return {
        algorithm:"",
        dateValue: '',
        min: minDate,
        max: maxDate,
        events: [],

        // json example
        eventsList: [
          {
            event: "bla",
            tweets_id:[
              "256292946331181056",
              "256334302034399232",
              "256335853738160128",
              "256346272506712064",
              "256346650132508673",
            ],
            dates:[
              "2022-05-27",
              "2022-05-27",
              "2022-05-26",
              "2022-05-05",
              "2022-05-27"
            ],
            dates_set: [
              "2022-05-27",
              "2022-05-26",
              "2022-05-05",
            ]
          },
            {event: "bla1",
              tweets_id:[
                  "256292946331181056",
                  "256334302034399232",
                  "256335853738160128",
                  "256346272506712064",
                  "256346650132508673"
              ],
               dates:[
              "2022-05-27",
              "2022-05-27",
              "2022-05-26",
              "2022-05-05",
              "2022-05-27"
              ],
              dates_set: [
                "2022-05-27",
                "2022-05-26",
                "2022-05-05",
              ]
            }
        ]
        //
      }
    },
    methods:{
    async getEventsByDate(){
      
      try{

        console.log("getEventsByDate method in EventsPage")
        console.log(" - Chosen algorithm: "+this.algorithm);

        const events_data=JSON.parse(localStorage.getItem("data_algorithm"))
        this.events=events_data
      } catch(error){

        let eventsFiltered = []
        this.eventsList.map( (eventObject) => {
          if (eventObject.dates_set.includes(this.dateValue)) {
            eventsFiltered.push(eventObject);
          }
        })
        this.events= eventsFiltered;
      }
    }},
    computed:{
        eventsByValue: function(){
            var filteredEvents = this.events.filter((event)=>{
                return event.date === this.value
            });
            return filteredEvents;
        }
    },
    created(){
        console.log("created ")
        this.algorithm = localStorage.getItem('algorithm');
        // this.getEvents();
    }

}
</script>

<style>
/* #Events-By-Date-Page{
    font-family: 'Balsamiq Sans', cursive;
    font-family: 'Merienda', cursive;
    text-align: center;
    background-color: whitesmoke;
    align-items: center;
} */
.events{
  display: block;
}
</style>