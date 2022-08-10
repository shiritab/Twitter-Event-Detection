<template>
  <div id="eventContainer">
      <h1>"{{ name }}"</h1>

      <div id="charts" style="">

      <EmotionEvent :emotion="emotion" :dates="dates"></EmotionEvent>
      <TweetsAmountByDate :dates="dates"></TweetsAmountByDate>
      </div>
      <br>
      <TweetD  :tweets="tweets" ></TweetD>
  </div>
</template>

<script>
import TweetD from "./TweetD.vue"
import EmotionEvent from "./charts/emotionEvent.vue"
import TweetsAmountByDate from "./charts/tweetsAmountByDate.vue"
export default {
    name: "Event",
    components:{
        TweetD,
        EmotionEvent,
        TweetsAmountByDate
    },
    props:{
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