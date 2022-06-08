<template>
  <div id="eventContainer">
      <h1>"{{ name }}"</h1>

      <div id="charts" style="">
      <!-- <Area :json_data="json_data"></Area> -->
      <EmotionEvent :emotion="emotion" :dates="dates"></EmotionEvent>
      <AreaEvent :dates="dates"></AreaEvent>
      </div>
      
      <TweetD  :tweets="tweets" ></TweetD>
  </div>
</template>

<script>
import TweetD from "./TweetD.vue"
import EmotionEvent from "./charts/emotion_event.vue"
import AreaEvent from "./charts/area_event.vue"
export default {
    name: "Event",
    components:{
        TweetD,
        EmotionEvent,
        AreaEvent
    },
    props:{
        id:{
            type: Number,
            require: true,
        },
        name: {
            type: String,
            require: true,
        },
        tweets:{
            type: Array,
        },
        dates:{
            type: Array,
        },
        emotion:{
            type: Array,
        },

    },
    data(){
        return{
            EventName: "Take a photo",
            tweetsList:[
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
        }
    },
    created(){
        console.log("created event");
        console.log(this.tweets);
    }
}
</script>

<style scoped>
    h1{
        font-style: italic;        
    }
    #eventContainer{
        text-align: center;
    }
    #charts{

    }
</style>