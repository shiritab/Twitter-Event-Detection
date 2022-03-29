<template id="Events-By-Date-Page">
  <div>
    <!-- <h1> Trending </h1> -->
    <br>
    <b-form-datepicker ref="datepicker"
    v-model="dateValue"
    :min="min"
    :max="max"
    @input="getEventsByDate()"
    style="width: 18.3rem; margin: auto"
    locale="en"></b-form-datepicker>
    <br>
    <b-card-group deck>
        <!-- <b-card v-for="event in eventsByValue"
            :key="event.id"
            style="max-width: 20rem; margin: auto;"
            bg-variant="light" class="text-center">
            <router-link :to="{ name: 'event', params:{id:event.id}}">
                <b-card-text>{{ event.name  }}</b-card-text>
            </router-link>
        </b-card> -->
        <b-card v-for="event in events"
            :key="event.event"
            style="max-width: 20rem; margin: auto;"
            bg-variant="light" class="text-center">
            <router-link :to="{ name: 'event', params:{id:event.event, tweets:event.tweets}}">
                <b-card-text>{{ event.event  }}</b-card-text>
            </router-link>
        </b-card>
    </b-card-group>
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
        dateValue: '',
        min: minDate,
        max: maxDate,
        events: [],

        // json example
        eventsList: [
          {
            event: "bla",
            tweets:[
                {
                id:"256292946331181056"
                },
                {
                id:"256334302034399232"
                },
                {
                id:"256335853738160128"
                },
                {
                id:"256346272506712064"
                },
                {
                id:"256346650132508673"
                },
            ],
          },
            {event: "bla1",
              tweets:[
                  {
                  id:"256292946331181056"
                  },
                  {
                  id:"256334302034399232"
                  },
                  {
                  id:"256335853738160128"
                  },
                  {
                  id:"256346272506712064"
                  },
                  {
                  id:"256346650132508673"
                  },
              ],}
            // {
            //     id: 123,
            //     event_name: "Take a photo",
            //     date: "2021-10-05",
            // },
            // {
            //     id: 2,
            //     event_name: "Elections day",
            //     date: "2021-06-01",
            // },
        ]
        //
      }
    },
    methods:{
    async getEventsByDate(){
      // pass
      try{
        // if(this.dateValue == "2021-10-05"){
        //   this.events = this.eventsList;
        // }
        console.log("here")
        const algorithm = localStorage.getItem('algorithm');
        console.log(algorithm);
        const response = await this.axios.get(
          `http://127.0.0.1:5000/events/${algorithm}/${this.dateValue}`
        );
        console.log(response)
        this.events =response.data;//.events;
      }catch(error){
        // console.log(error);
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
</style>