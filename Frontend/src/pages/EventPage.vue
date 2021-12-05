<template>
  <div>
      <Event :id="1" :name="$route.params.id" :tweets="tweets"></Event>
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
        tweets:{
            type: Array,
            required: true,
        }
    },
    created(){
        console.log("created event page");
        console.log(this.tweets);
    }
}
</script>

<style>

</style>