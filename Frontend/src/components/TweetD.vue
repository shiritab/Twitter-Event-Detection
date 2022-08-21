<template>
  <div>
    <div  class="container" >
      <div class="row ">
        <Tweet v-for="tweet in tweets_to_show"
          :key="tweet"
          :id="tweet"
          error-message="This tweet could not be loaded"
          class = "tweets_class"
          >
        </Tweet>
      </div>

      <b-pagination style="display:inline-flex"
        v-model="currentPage"
        :total-rows="tweets.length"
        :per-page=12
        :align="center"
        aria-controls="tweets-show"
        @change="onPageChange"
        >
      </b-pagination> 
    </div>
  </div>
</template>

<script>
import { Tweet } from 'vue-tweet-embed'

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
      tweets_to_show:this.tweets.slice(0,12),
      currentPage: 1
    }
  },
  methods:{
    onPageChange(page){
      /** Each page contains at most 12 tweets */
      this.tweets_to_show=this.tweets.slice(page*12-12,page*12)
    },
    sortTweetIds(){
      this.tweets = this.tweets.sort();
    }
  },
 created(){
  this.sortTweetIds();
 }
 
}
</script>


<style>
.tweets_class{
  display: inline-block;
  position: relative;
  padding: 2px;
}
.row col{
  max-height: 10px;
}
.searchRes{
  overflow-x: hidden;
  overflow-y:scroll;
  max-height: fit-content;

}

</style>