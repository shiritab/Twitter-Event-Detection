<template>
  <div>
      <Event :name="name" :tweets="tweets" :emotion="emotion" :dates="dates"></Event>
  </div>
</template>

<script>
import Event from "./../components/Event.vue"
export default {
    name: "EventPage",
    components:{
        Event,
    },
    props:{
        name:{
            type: String
        },
        tweets:{
            type: Array,
            required: true,
        },
        dates:{
            type: Array,
        },
        emotion:{
            type: Array,
        },
    },
    created(){
        console.log("created event page");
        console.log(this.emotion);
    }
}
</script>

<style>

</style>