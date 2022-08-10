import  flask
#
class TwitterCollector:
    '''
    Given a set of tweets' ids we collect the tweets' data from twitter api.
    '''
    def __init__(self):
        pass
    def read_from_twitter(self,text_path=r"C:\Users\meiri\Documents\GitHub\Twitter-Event-Detection\Backend\data\main_files\list_of_tweets.txt",output_json="tweets_from_api.txt"):

        # Import the necessary package to process data in JSON format
        try:
            import json
        except ImportError:
            import simplejson as json

        # Import the tweepy library
        import tweepy

        # Variables that contains the user credentials to access Twitter API


        ACCESS_TOKEN = '1125144535191912449-8kYloZrLovkfszeCa7VnjGPHiRPwqk'
        ACCESS_SECRET = 'Bw23q3MCvicvW1V0sZpyCte8PGOJk3ZPI5EuLS0UnrXEu'
        CONSUMER_KEY = 'Ofk4zDYPQqyBdNnNADo504kB5'
        CONSUMER_SECRET = '07iel8TpwbVnZjQ1uWtKYcZynPcOEb2kuE2a3fK4xzjVuWOhYe'

        # Setup tweepy to authenticate with Twitter credentials:

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Create the api to connect to twitter with your creadentials
        api = tweepy.API(auth, wait_on_rate_limit=True)
        # ---------------------------------------------------------------------------------------------------------------------
        # wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
        # wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
        # ---------------------------------------------------------------------------------------------------------------------

        # ---------------------------------------------------------------------------------------------------------------------
        # The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends.
        # This is the equivalent of /timeline/home on the Web.
        # ---------------------------------------------------------------------------------------------------------------------

        # tweet = api.get_status(1452670807373721613)
        # print(tweet._json)

        # for status in tweepy.Cursor(api.home_timeline).items(20):
            # tweets_file = open(tweets_filename, "w")
            # print(str(status._json["id"]))

            # print(status._json["tweet_id"])
            # with open(tweets_filename, 'w') as outfile:
            #     json.dump(status._json, outfile)


        # ---------------------------------------------------------------------------------------------------------------------
        # Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc.
        # To help make pagination easier and Tweepy has the Cursor object.
        # ---------------------------------------------------------------


        # We use the file saved from last step as example
        data=[]
        with open("output_file_new", 'w') as output_file:
            # for line in input_file.readlines():
            #     print(line)
            #     tweet = api.get_status(line)
            for tweet in api.search(q="Python",lang="en", rpp=10):
                print(f"{tweet.user.name}:{tweet.text}")
                print(tweet._json)
                data.append(tweet._json)
                output_file.write(tweet)


        # with open("data.json", 'a') as filehandle:
        #     filehandle.write("%s\n" % json.dumps(tweet._json))
        # #
        # with open(output_json, 'w') as outfile:
        #    json.dump(data,outfile)



        # tweets_file = open(output_json, "r")
        # for line in tweets_file:
        #     try:
        #         # Read in one line of the file, convert it into a json object
        #         tweet = json.loads(line.strip())
        #         if 'text' in tweet:  # only messages contains 'text' field is a tweet
        #             print(tweet['id'])  # This is the tweet's id
        #             print(tweet['created_at'])  # when the tweet posted
        #             print(tweet['text'])  # content of the tweet
        #
        #             print( tweet['user']['id'])  # id of the user who posted the tweet
        #             print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
        #             print(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"
        #
        #             hashtags = []
        #             for hashtag in tweet['entities']['hashtags']:
        #                 hashtags.append(hashtag['text'])
        #             print(hashtags)
        #
        #     except:
        #         # read in a line is not in JSON format (sometimes error occured)
        #         continue
