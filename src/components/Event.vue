<template>
  <div id="eventContainer">
      <h1>"{{ EventName }}"</h1>
      <br>
      <Tweet :tweets="tweetsList"></Tweet>
  </div>
</template>

<script>
import Tweet from "./Tweet.vue"
export default {
    name: "Event",
    components:{
        Tweet,
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
                    id: 1,
                    date: "05/10/2021",
                    content: "@shirit: I just posted a photo yesterday."
                },
                {
                    id: 2,
                    date: "05/10/2021",
                    content: "@guygool: Today I am having a photoshoot for LinkedIn profile pic."
                },
                {
                    id: 3,
                    date: "05/10/2021",
                    content: "@nivmeir: My fiance and I took a picture of us in the USA."
                },
                {
                    id: 4,
                    date: "05/10/2021",
                    content: "@nivmeir: link to our new photo https://fb.com/nivmeir/123%73?USA."
                },
            ],
        }
    },
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