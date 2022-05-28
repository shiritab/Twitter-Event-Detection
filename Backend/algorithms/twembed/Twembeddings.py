import json
import os
import sys
from . import *
from .clustering import main
# from ...summarization import hugging_faces
# from ...utils_backend.emotion_tweet import EmotionTweet
import pandas as pd

TAGGED_TWEETS_PATH = f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv'

class Twembeddings(DetectionAlgorithm):


    def __init__(self):
        self.results_path = "../results/twembeddings/"
        self.eventResutls = ""
        self.data = ""

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
        super().summarize()