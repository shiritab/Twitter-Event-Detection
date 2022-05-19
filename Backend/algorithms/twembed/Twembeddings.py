import json
import os
import sys
from . import *
from .clustering import main
from ...summarization import hugging_faces
from ...utils_backend.emotion_tweet import EmotionTweet
import pandas as pd

TAGGED_TWEETS_PATH = f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv'

class Twembeddings(DetectionAlgorithm):

    results_path = "../results/twembeddings/"
    data = ""

    def __init__(self):
        super().__init__()

    def run_algorithm(self, data):
        self.data = data
        file_results = self.results_path + "results_{}".format(data)
        if os.path.isfile(file_results):
            with open(file_results, "r") as results_file:
                self.eventResutls = json.load(results_file)
                return

        if data == "event2012.json":
            data = TAGGED_TWEETS_PATH
        else:
            data = "../data/uploaded/" + data
        self.eventResutls = main({'model': ['tfidf_all_tweets'],
              'dataset':data,
              'lang': 'en',
              'annotation': 'no',
              'threshold': ['0.7'],
              'batch_size': None,
              'remove_mentions': None,
              'window': 24})

        with open(self.results_path + "results_{}".format(data) , "w") as file_results:
            json.dump(self.eventResutls, file_results)


    def summarize(self):
        if os.path.isfile(self.results_path + "summarized_{}".format(self.data)):
            with open (self.results_path + "summarized_{}".format(self.data), "r") as summarized_file:
                return json.load(summarized_file)

        print("started summarize twembeddings")
        data=self.eventResutls
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
            sys.stdout.write('\r' + "summarizing processing: {}/{}".format(i,len(data)))
            sys.stdout.flush()
        with open(self.results_path + "summarized_{}".format(self.data), 'w') as summarized_file:
            json.dump(data, summarized_file)

        print("done summarize twembeddings")
        return data