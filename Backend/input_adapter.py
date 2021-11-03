import json
import tweet_cleaner
import re


class Adapter:

    def __init__(self):
        self.entity_extractor = tweet_cleaner.EntityExtractor()
        self.tweet_cleaner = tweet_cleaner.TweetCleaner()


    def convert_input(self,input_type,output_type,input_file=None):
        if( input_type=="twitter_js" and output_type=="sedtwix"):
            return self.from_twitter_to_sedtwik(input_file)


    def from_twitter_to_sedtwik(self,input_json="tweets_from_api.txt",output_file="Sedtwik_input.json"):
        cleaner=tweet_cleaner.TweetCleaner()
        data_to_output = []
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
                        tweet_to_write["entities"]={}
                        mentions_list=re.findall(r'(?:(?<=\s)|(?<=^))@.*?(?=\s|$|\.)', tweet['text'])
                        hashtags_list=re.findall(r'(?:(?<=\s)|(?<=^))#.*?(?=\s|$|\.)', tweet['text'])
                        tweet_to_write['entities']['hashtags'] = [h[1:] for h in hashtags_list]
                        tweet_to_write['entities']['user_mentions'] = [m[1:] for m in mentions_list]
                        print(tweet_to_write)
                        data_to_output.append(tweet_to_write)

                except BaseException as err:

                    print(f"Unexpected {err=}, {type(err)=}")
                    # read in a line is not in JSON format (sometimes error occured)
                    continue

        with open(output_file, 'w') as filehandle:
            filehandle.writelines("%s\n" % json.dumps(j) for j in data_to_output)



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

