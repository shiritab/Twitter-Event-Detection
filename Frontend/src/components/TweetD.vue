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

<template>
  <b-container class="bv-example-row">
    <b-row >
      <b-col class="row">
        <Tweet  v-for="tweet in tweets"
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
  props:{
        tweets:{
            type: Array,
            require: true,
        }
  },
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