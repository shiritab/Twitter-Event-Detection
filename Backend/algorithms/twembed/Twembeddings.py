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
        results = self.get_results(data)
        if results:
            return results

        if data == "event2012.json":
            dataset = TAGGED_TWEETS_PATH
        else:
            dataset = "../data/uploaded/" + data
        self.eventResutls = main({'model': ['tfidf_all_tweets'],
              'dataset':dataset,
              'lang': 'en',
              'annotation': 'no',
              'threshold': ['0.7'],
              'batch_size': None,
              'remove_mentions': None,
              'window': 24})

        self.save_results(data)

