<template>
  <div id="eventContainer">
      <h1>"{{ name }}"</h1>
      <br>
      <!-- <Tweet :tweets="tweetsList"></Tweet> -->
      <TweetD  :tweets="tweets"></TweetD>
  </div>
</template>

<script>
import TweetD from "./TweetD.vue"
export default {
    name: "Event",
    components:{
        TweetD,
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
        }
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
</style>