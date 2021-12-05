<template>
  <div>
    <br>
    <b-form-datepicker ref="datepicker"
    v-model="value"
    :min="min"
    :max="max"
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
        <b-card v-for="event in eventsByValue"
            :key="event.event_name"
            style="max-width: 20rem; margin: auto;"
            bg-variant="light" class="text-center">
            <router-link :to="{ name: 'event', params:{id:event.event_name}}">
                <b-card-text>{{ event.event_name  }}</b-card-text>
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
      minDate.setMonth(minDate.getMonth() - 2);
      minDate.setDate(1);

      const maxDate = new Date(today)

      return {
        value: '',
        min: minDate,
        max: maxDate,
        events: [
            {
                id: 123,
                event_name: "Take a photo",
                date: "2021-10-05",
            },
            {
                id: 2,
                event_name: "Elections day",
                date: "2021-06-01",
            },
        ]
      }
    },
    methods:{
    async getEvents(){
      try{
        const response = await this.axios.get(
          `http://127.0.0.1:5000/events/summary`
        );
        console.log(response)
        this.events =response.data.events;
      }catch(error){
        console.log(error);
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

</style>