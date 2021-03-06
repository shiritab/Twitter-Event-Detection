class Segment:
    def __init__(self,segment):
        """
        segment           - string of words ex. 'steve jobs'
        """
        self.tweet_ids=[]
        self.segment = segment
        self.tweets = [] # list of tweets( text:str ) containing this segment in current time window
        self.dirty_tweets = [] # list of tweets( text:str ) containing this segment in current time window

        self.dates=[]
        self.freq = 0 # tweet-freq i.e. number of tweets containing this segment
        self.user_set = set() # no. of unique users that used this segment in current time window
        self.retweet_count = 0 # sum of retweet counts of all tweets containing this segment
        self.followers_count = 0 # sum of followers count of all users using this segment
        self.newsworthiness = 0 # measure of importance of segment calculated by Twevent's Q(s) values

    def __str__(self):
        return 'Segment:'+self.segment+', freq:'+str(self.freq)+', user_count:'+str(self.get_user_count())

    def add_tweet(self,tweet_id,user_id, text, retweet_count, followers_count,date,dirty_text):
        self.tweets.append(text)
        self.dirty_tweets.append(dirty_text)
        self.tweet_ids.append(tweet_id)
        self.user_set.add(user_id)
        self.freq += 1
        self.dates.append(date)
        self.retweet_count += retweet_count
        self.followers_count += followers_count

    def get_user_count(self):
        return len(self.user_set)

