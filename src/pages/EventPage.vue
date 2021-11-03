<template>
  <div>
      <Event :id="1" :name="'Take a photo'"></Event>
  </div>
</template>

<script>
import Event from "./../components/Event.vue"
export default {
    name: "EventPage",
    components:{
        Event,
    }
}
</script>

<style>

</style>