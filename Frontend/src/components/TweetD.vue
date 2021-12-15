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
<div>



  <b-container id="tweets-show" class="bv-example-row">
    <b-row >
      <b-col class="row">
        <Tweet v-for="tweet in tweets_to_show"
        :key="tweet"
        :id="tweet"
      
        class = "tweets_class"
        >
        </Tweet>
      </b-col>
    </b-row>
  </b-container>  
  <!-- <Tweet id="692527862369357824" style="width: 5px; padding: 2px;">
    <div class="spinner"></div>
  </Tweet> -->

    <b-pagination style="display:inline-flex"
      v-model="currentPage"
      :total-rows="tweets.length"
      :per-page=10
      :align="center"
      aria-controls="tweets-show"
      @change="onPageChange"
    ></b-pagination>
</div>
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
  data()  {

return{
  tweets_to_show:this.tweets.slice(0,10),
  currentPage:1
}

  },
  methods:{
    onPageChange(page){
      console.log(page)
      
      this.tweets_to_show=this.tweets.slice(page*10-10,page*10)


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