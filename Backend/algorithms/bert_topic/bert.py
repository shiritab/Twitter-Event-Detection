import json
import os
import sys
from time import strftime
from bertopic import BERTopic
import torch
from ..abstractEventDetectionAlgorithm import DetectionAlgorithm
import pandas as pd
import pickle
import random
from tqdm.notebook import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
from bertopic import BERTopic
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from itertools import product
from tqdm import tqdm_notebook as tqdm
from ...summarization import hugging_faces
from ...utils_backend.emotion_tweet import EmotionTweet

torch.cuda.is_available()
PICKLE_FILE = "../data/tagged_tweets.pkl"


def load_data(data):
    """
    :param data: Import data file from data2012 or from user files
    :return:
    """
    if data == "event2012.json":
        path_file = PICKLE_FILE
    else:
        path_file = "../data/uploaded/" + data
    with open(path_file, "rb") as f:
        df = pickle.load(f)
    return df


class Bert(DetectionAlgorithm):

    def __init__(self):
        """
        result_path : The path for the result to be saved
        event_results: The algorithm's results
        data_name: The of the executed data
        """
        self.results_path = "../results/bert_topic/"
        self.event_results = ""
        self.data_name = ""

    def run_algorithm(self, data_name):
        """
        :param data_name:
        :return:
        """
        results = self.get_results(data_name)
        # already exist in the system
        if results:
            return results

        results = self.create_output()
        self.save_results(data_name)
        return results

    def get_topic_model(self, documents, n_neighbors, min_topic_size, calculate_probabilities=False):
        """
        :param documents:
        :param n_neighbors:
        :param min_topic_size:
        :param calculate_probabilities:
        :return:
        """
        umap_model = UMAP(n_neighbors=n_neighbors, n_components=10, min_dist=0.0, metric='cosine')

        vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")  # , min_df=10)
        topic_model = BERTopic(umap_model=umap_model, vectorizer_model=vectorizer_model,
                               calculate_probabilities=calculate_probabilities, verbose=True,
                               min_topic_size=min_topic_size)
        topic_model.fit(documents)
        return topic_model

    def create_topic(self):
        df = load_data(self.data_name)
        content = list(df["text"])
        random.seed(1)
        docs = random.sample(content, 20000)
        n_neighbors = [5]
        min_topic_sizes = [50]

        res = []
        for n_neighbor, min_topic_size in tqdm(product(n_neighbors, min_topic_sizes)):  # , total=36):
            model = self.get_topic_model(docs, n_neighbor, min_topic_size)
            topics, probas = model.transform(df["text"])
            df["topic"] = topics
            tmp = df[["text", "topic", "tweet_id", "date"]]
            tmp["date"] = tmp["date"].apply(lambda date: date.strftime('%Y-%m-%d'))
            tmp["ID"] = range(len(df))
            print(tmp.head())
            print([topic for topic in tmp.groupby('topic')])

        return tmp

    def create_output(self):
        """
        :return: Json file the containt tweet's data- event, date,dirty text ,tweet_id
        """
        tmp = self.create_topic()
        events = []
        for topic in tmp.groupby('topic'):
            topic = topic[1]
            events.append({
                'event': None,
                'tweets': [id for id in topic['tweet_id']],
                'dirty_text': [text for text in topic['text']],
                'dates': [date for date in topic['date']],
            })
            events[len(events) - 1]['dates_set'] = list(set(events[len(events) - 1]['dates']))

        self.event_results = events
        return events
