import json
import os
import sys

from . import *
from .clustering import main
from ...summarization import hugging_faces
from ...utils_backend.emotion_tweet import EmotionTweet
import pandas as pd


class Twembeddings(DetectionAlgorithm):

    results_path = "../results/twembeddings/"

    def __init__(self):
        super().__init__()

    def run_algorithm(self, data):
        file_results = self.results_path + "events_results.json"
        if os.path.isfile(file_results):
            with open(file_results, "r") as results_file:
                self.eventResutls = json.load(results_file)
                return

        self.eventResutls = main({'model': ['tfidf_all_tweets'],
              # 'dataset': 'data/event2012json_2.tsv',
              'dataset':data,
              'lang': 'en',
              'annotation': 'no',
              'threshold': ['0.7'],
              'batch_size': None,
              'remove_mentions': None,
              'window': 24})

        with open(self.results_path + "events_results.json", "w") as file_results:
            json.dump(self.eventResutls, file_results)

    # TODO: Save results to self.eventResults

    def summarize(self):
        if os.path.isfile(self.results_path + "summarized.json"):
            with open (self.results_path + "summarized.json", "r") as summarized_file:
                return json.load(summarized_file)

        print("started summarize twembeddings")
        data=self.eventResutls
        # if data[0]['summarized'] == "true":
        #     return data
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
        with open(self.results_path + "summarized.json", 'w') as summarized_file:
            json.dump(data, summarized_file)

        print("done summarize twembeddings")
        return data