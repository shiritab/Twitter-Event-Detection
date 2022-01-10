from textblob import TextBlob

class EmotionTweet:
    
    def find_emotion(self, tweets_list):
        '''
        This methods iterates over each tweet in tweets_list and saves it's sentiment value in the range of [-1,1].
        @param tweets_list: string[]
        return float[]
        '''
        tweets_emotion = []
        for tweet in tweets_list:
            sentiment = TextBlob(tweet).sentiment.polarity
            tweets_emotion.append( sentiment)
        return tweets_emotion
