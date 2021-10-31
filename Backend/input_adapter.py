import json
import tweet_cleaner
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

    def from_twitter_to_sedtwik(self,input_json="tweets_from_api.txt",output_file="sed.json"):
        cleaner=tweet_cleaner.TweetCleaner()
        data_to_output=[]
        with open(input_json) as json_file:
            data = list(json.load(json_file))
            for tweet in data:
                tweet_to_write = {}

                try:
                    # Read in one line of the file, convert it into a json object
                    if 'text' in tweet:  # only messages contains 'text' field is a tweet

                        tweet_to_write['created_at']=tweet['created_at']
                        # tweet_to_write['text']=tweet['text']
                        tweet_to_write['text'] = cleaner.get_cleaned_text(tweet['text'])

                        tweet_to_write['user']= {"id":tweet['user']['id'],"followers_count":tweet['user']['followers_count']}
                        tweet_to_write['retweet_count']= tweet['retweet_count']

                        tweet_to_write['entities']= {"hashtags":tweet['entities']['hashtags'],"user_mentions":tweet['entities']['user_mentions']}
                        print(tweet_to_write)
                        data_to_output.append(tweet_to_write)



                except BaseException as err:

                    print(f"Unexpected {err=}, {type(err)=}")
                    # read in a line is not in JSON format (sometimes error occured)
                    continue
        with open(output_file, 'a') as filehandle:
            filehandle.writelines("%s\n" % json.dumps(j) for j in data_to_output)




    # def convert_df_into_jsons(posts_df, authors_df):
    #
    #     mentions_list = posts_df['text'].str.findall(r'(?:(?<=\s)|(?<=^))@.*?(?=\s|$|\.)')
    #     hashtags_list = posts_df['text'].str.findall(r'(?:(?<=\s)|(?<=^))#.*?(?=\s|$|\.)')
    #     posts_jsons = json.loads(posts_df.to_json(orient="records"))
    #     users_jsons = json.loads(authors_df.to_json(orient="records"))
    #     for json_tweet, json_user, mentions, hashtags in zip(posts_jsons, users_jsons, mentions_list, hashtags_list):
    #         json_tweet['user'] = json_user
    #         json_tweet['entities'] = {}
    #         json_tweet['entities']['hashtags'] = [h[1:] for h in hashtags]
    #         json_tweet['entities']['user_mentions'] = [m[1:] for m in mentions]
    #         json_tweet['cleaned_text'] = tweet_cleaner.get_cleaned_text(json_tweet['text'])
    #         # json_tweet['named_entities'] = list(map(str,(nlp(json_tweet['text']).ents)))
    #     posts_jsons = entity_extractor.apply(posts_jsons)
    #     return posts_jsons
    #
    # def save_jsons_to_file(file_path, data_df, posts_fields, authors_fields):
    #     posts_df, authors_df = data_df[posts_fields], data_df[authors_fields]
    #     posts_jsons = convert_df_into_jsons(posts_df, authors_df)
    #
    #     with open(file_path, 'a') as filehandle:
    #         filehandle.writelines("%s\n" % json.dumps(j) for j in posts_jsons)

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

