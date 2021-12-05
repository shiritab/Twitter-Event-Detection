<!--<template>
    <b-card-group deck>
      <b-card v-for="tweet in tweets"
        :key="tweet.id"
        style="max-width: 20rem; margin: auto;"
        bg-variant="light" :header="tweet.date" class="text-center">
        <b-card-text>{{ tweet.content }}</b-card-text>
      </b-card>
    </b-card-group>
</template>

<script>
export default {
    name: "Tweet",
    props:{
        tweets:{
            type: Array,
            require: true,
        }
    }
}
</script>

<style scope>

</style>-->
<!--<template>
  <Tweet
    tweet-id="1370027087818461184"
    cards="visible"
    conversation="all"
    lang="en"
    theme="light"
    align="left"
    :width="400"
    :dnt="false"
    @tweet-load-error="onTweetLoadError"
    @tweet-load-success="onTweetLoadSuccess"
  >
    <template v-slot:loading>
      <span>Loading...</span>
    </template>

    <template v-slot:error>
      <span>Sorry, that tweet doesn’t exist!</span>
    </template>
  </Tweet>
</template>

<script>
import { defineComponent } from 'define-component'
import Tweet from 'vue-tweet'

export default defineComponent({
  components: {
    Tweet
  },
  setup() {
    function onTweetLoadSuccess(embedNode) {
      console.log(embedNode)
    }

    function onTweetLoadError() {
      console.log("Oops... an error has occurred")
    }

    return { onTweetLoadSuccess, onTweetLoadError }
  }
})
</script>-->
<template>
  <b-container class="bv-example-row">
    <b-row >
      <b-col class="row">
        <Tweet v-for="tweet in tweets"
        :key="tweet.id"
        :id="tweet.id"
        class = "tweets_class"
        >
        </Tweet>
      </b-col>
    </b-row>
  </b-container>  
  <!-- <Tweet id="692527862369357824" style="width: 5px; padding: 2px;">
    <div class="spinner"></div>
  </Tweet> -->
</template>

<script>import { Tweet } from 'vue-tweet-embed'

export default{
  name: "TweetD",
  components:{
    Tweet
  },
  data(){
    return{
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
    }
  }
}
</script>


<style>
.tweets_class{
  display: inline-block;
  position: relative;
  padding: 10px;
}
.row col{
  max-height: 10px;
}
</style>