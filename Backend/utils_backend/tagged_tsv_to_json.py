import json
import pandas as pd

tagged_tweets = f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv'
tagged_tweets_df = pd.read_csv(tagged_tweets, sep='\t')
year = 2012
MONTHS = {'Oct':"10", 'Nov':"11"}

requested_cols = list(tagged_tweets_df.columns)[1:4]
tagged_tweets_df = tagged_tweets_df[requested_cols]
tagged_tweets_df = tagged_tweets_df.rename(columns = {"id":"tweet_id"})
print(tagged_tweets_df)


def to_json():
    with open('../data/tagged_tweets/tagged_tweets_dir/tagged_tweets.json', 'w') as outfile:
        for i in range(len(tagged_tweets_df)):
            line = tagged_tweets_df.iloc[i]
            add_to_json = {"tweet_id":str(line["tweet_id"]), "text":line["text"], "created_at":line["created_at"]}
            outfile.write(json.dumps(add_to_json) + '\n')

def collect():
    count = 0
    not_found_file = '../data/tagged_tweets/not_found_tagged_tweets.json'
    with open('../data/tagged_tweets/tagged_tweets_dir/tagged_tweets.json', 'w') as outfile:
        for i in range(len(tagged_tweets_df)):
            line = tagged_tweets_df.iloc[i]
            month = MONTHS[line["created_at"][4:7]]
            day = line["created_at"][8:10]
            hour = line["created_at"][11:13]
            dir_name = "\{}-{}-{}".format(year,month,day)
            file_name = "\{}_hour.json".format(hour)
            file_path = 'C:\\Users\\user\\Documents\\GitHub\\Twitter-Event-Detection\\Backend\\data\\try_scan_tweets{}{}'.format(dir_name,file_name)
            try:
                with open(file_path, 'r') as file:
                    found = False
                    while not found:
                        line_2 = file.readline()
                        if line_2 == '': break
                        tweet = json.loads(line_2)
                        if tweet["tweet_id"] == str(line["tweet_id"]):
                            found = True
                            outfile.write(json.dumps(tweet) + '\n')
                            count+=1
            except Exception as e:
                with open(not_found_file, 'a') as file:
                    file.write(str(line["tweet_id"])+"\n")
                    continue
    print(count)
