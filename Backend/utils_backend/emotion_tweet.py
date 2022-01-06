from textblob import TextBlob

class EmotionTweet:
    def find_emotion(self, tweets_list):
        tweets_emotion = []
        for tweet in tweets_list:
            sentiment = TextBlob(tweet).sentiment.polarity
            tweets_emotion.append( sentiment)
        return tweets_emotion