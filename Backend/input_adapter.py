import json
class Adapter:

    def __init__(self):
        pass


    def convert_input(self,input_type,output_type,input_file=None):
        if( input_type=="twitter_js" and output_type=="sedtwix"):
            return self.from_twitter_to_sedtwik(input_file)
    # @staticmethod
    # def from_twitter_to_sedtwik(input_json):
    #
    #     try:
    #         import json
    #     except ImportError:
    #         import simplejson as json
    #
    #     # We use the file saved from last step as example
    #
    #     for line in input_json:
    #         try:
    #             # Read in one line of the file, convert it into a json object
    #             tweet = json.loads(line.strip())
    #             if 'text' in tweet:  # only messages contains 'text' field is a tweet
    #                 print(tweet['id'])  # This is the tweet's id
    #                 print(tweet['created_at'])  # when the tweet posted
    #                 print(tweet['text'])  # content of the tweet
    #
    #                 print(tweet['user']['id'])  # id of the user who posted the tweet
    #                 print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
    #                 print(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"
    #
    #                 hashtags = []
    #                 for hashtag in tweet['entities']['hashtags']:
    #                     hashtags.append(hashtag['text'])
    #                 print(hashtags)
    #
    #         except:
    #             # read in a line is not in JSON format (sometimes error occured)
    #             continue
    @staticmethod
    def from_twitter_to_sedtwik(input_json="tweets_from_api.txt"):
        with open(input_json) as json_file:
            data = list(json.load(json_file))
            for tweet in data:
                try:
                    # Read in one line of the file, convert it into a json object
                    if 'text' in tweet:  # only messages contains 'text' field is a tweet
                        print(tweet['id'])  # This is the tweet's id
                        print(tweet['created_at'])  # when the tweet posted
                        print(tweet['text'])  # content of the tweet

                        print(tweet['user']['id'])  # id of the user who posted the tweet
                        print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
                        print(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"

                        hashtags = []
                        for hashtag in tweet['entities']['hashtags']:
                            hashtags.append(hashtag['text'])
                        print(hashtags)

                except:
                    # read in a line is not in JSON format (sometimes error occured)
                    continue

    @staticmethod
    def from_json_to_db():
        pass

    @staticmethod
    def from_db_to_json():
        pass

    @staticmethod
    def from_tsv_to_db():
        pass

    @staticmethod
    def from_db_to_tsv():
        pass

    def excute_sedtwik(self):
        pass

