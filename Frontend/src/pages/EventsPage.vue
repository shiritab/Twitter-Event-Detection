<template id="Events-By-Date-Page">
  <div>
    <br>
    <p>Events by algorithm: {{this.algorithm}}</p>
    <b-form-datepicker ref="datepicker"
      v-model="dateValue"
      :min="min"
      :max="max"
      @input="getEventsByDate()"
      style="width: 18.3rem; margin: auto"
      locale="en">
    </b-form-datepicker>
    <br>
    <div class="row">
      <b-card v-for="event in events"
          :key="event.event"
          style="max-width: 20rem; margin: auto;"
          bg-variant="light" 
          class="text-center">

          <router-link :to="{ name: 'event', params:{name:event.event, tweets:event.tweets,dates:event.dates,emotion:event.tweets_emotion}}">
              <b-card-text>{{ event.event  }}</b-card-text>
          </router-link>

      </b-card>
    </div>
    
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
        algorithm: "",
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
      }
    },
    methods:{

      getEventsByDate(){
        /* filters all events that occured on chose date */
        
        this.events = [];
        try{
          console.log(" - Chosen algorithm: "+this.algorithm);

          const events_data=JSON.parse(localStorage.getItem("data_algorithm"))

          let eventsFiltered = []
          events_data.map( (eventObject) => {
            if (eventObject.dates_set.includes(this.dateValue)) {
              eventsFiltered.push(eventObject);
            }
          })

          this.events=eventsFiltered

        } catch(error){
          let eventsFiltered = []
          this.eventsList.map( (eventObject) => {
            if (eventObject.dates_set.includes(this.dateValue)) {
              eventsFiltered.push(eventObject);
            }
          })
          this.events= eventsFiltered;
          console.log(`error occured on getEventsByDate EventsPage. error: ${error}`);
        }

      }
    },

    created(){
        console.log("created ")
        this.algorithm = localStorage.getItem('algorithm');
    }

}
</script>

<style>
.events{
  display: block;
}
</style>