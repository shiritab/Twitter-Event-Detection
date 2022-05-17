import json

from . import *
from ...summarization import hugging_faces
from ...utils_backend.emotion_tweet import EmotionTweet


class Twembeddings(DetectionAlgorithm):
    def __init__(self):
        super().__init__()

    def run_algorithm(self, *data):
        main({'model': ['tfidf_all_tweets'],
              # 'dataset': 'data/event2012json_2.tsv',
              'dataset':data,
              'lang': 'en',
              'annotation': 'no',
              'threshold': ['0.7'],
              'batch_size': None,
              'remove_mentions': None,
              'window': 24})

        sort_results_by_cluster("data/event2012json_2_results.tsv")

    def summarize(self):
        data=self.eventResutls
        if data[0]['summarized'] == "true":
            return data
        hg = hugging_faces.HuggingFaces()
        for i in range(len(data)):
            # summarize for event name
            dictionary = data[i]
            summary = hg.summarize(dictionary["dirty_text"])
            # calc tweet emotion
            if "tweets_emotion" not in dictionary:
                dictionary["tweets_emotion"] = EmotionTweet().find_emotion(dictionary["dirty_text"])
            dictionary['event'] = summary
            data[i] = dictionary
        # with open(f"results_{}", 'w') as file:
        #     json.dump(data, file)
        return data



