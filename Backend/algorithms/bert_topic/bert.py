import json
import os
import sys
from bertopic import BERTopic
import torch
from ..eventDetectionAlgorithm import DetectionAlgorithm
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


def load_data():
    with open(PICKLE_FILE, "rb") as f:
        df = pickle.load(f)
    return df


class Bert(DetectionAlgorithm):
    results_path = "../results/bert_topic/"

    def run_algorithm(self, *data):
        if os.path.isfile(self.results_path + "events_results.json"):
            with open(self.results_path + "events_results.json", "r") as results_file:
                self.eventResutls = json.load(results_file)
                return

        return self.create_output()

    def summarize(self):
        if os.path.isfile(self.results_path + "summarized.json"):
            with open (self.results_path + "summarized.json", "r") as summarized_file:
                return json.load(summarized_file)

        print("started summarize bert-topic")
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

        print("done summarize bert-topic")
        return data

    def get_topic_model(self, documents, n_neighbors, min_topic_size, calculate_probabilities=False):
        umap_model = UMAP(n_neighbors=n_neighbors, n_components=10, min_dist=0.0, metric='cosine')

        vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")  # , min_df=10)
        topic_model = BERTopic(umap_model=umap_model, vectorizer_model=vectorizer_model,
                               calculate_probabilities=calculate_probabilities, verbose=True,
                               min_topic_size=min_topic_size)
        topic_model.fit(documents)
        return topic_model

    def get_coherence(self, df, topic_model):
        documents_per_topic = df.groupby(['topic'], as_index=False).agg({'text': ' '.join})

        cleaned_docs = topic_model._preprocess_text(documents_per_topic.text.values)

        # Extract vectorizer and analyzer from BERTopic
        vectorizer = topic_model.vectorizer_model
        analyzer = vectorizer.build_analyzer()

        # Extract features for Topic Coherence evaluation
        words = vectorizer.get_feature_names()
        tokens = [analyzer(doc) for doc in cleaned_docs]
        dictionary = corpora.Dictionary(tokens)
        corpus = [dictionary.doc2bow(token) for token in tokens]
        topic_words = [[words for words, _ in topic_model.get_topic(topic)]
                       for topic in range(len(set(topics)) - 1)]

        # Evaluate
        coherence_model = CoherenceModel(topics=topic_words,
                                         texts=tokens,
                                         corpus=corpus,
                                         dictionary=dictionary,
                                         )  # coherence='c_v')
        coherence = coherence_model.get_coherence()
        return coherence

    def create_topic(self):
        df = load_data()
        content = list(df["text"])
        random.seed(1)
        docs = random.sample(content, 20000)
        n_neighbors = [5]  # , 10 ]#,15, 20, 25, 30, 35, 40, 45]
        min_topic_sizes = [50]  # , 100 ]#,150, 200, 250, 300, 350 , 400]

        res = []
        for n_neighbor, min_topic_size in tqdm(product(n_neighbors, min_topic_sizes)):  # , total=36):
            model = self.get_topic_model(docs, n_neighbor, min_topic_size)
            topics, probas = model.transform(df["text"])
            df["topic"] = topics
            tmp = df[["text", "topic", "tweet_id"]]
            tmp["ID"] = range(len(df))
            print(tmp.head())
            print([topic for topic in tmp.groupby('topic')])
            # coh = get_coherence(tmp, model)
            # res.append({"coherenc": coh, "min_topic_size": min_topic_size, "n_neighbor":n_neighbor})
            # pd.DataFrame(res).to_csv("coher.csv")
        return tmp

    def create_output(self):
        tmp = self.create_topic()
        events = []
        for topic in tmp.groupby('topic'):
            topic = topic[1]
            events.append({
                'event': None,
                'tweets': [id for id in topic['tweet_id']],
                'dirty_text': [text for text in topic['text']]
            })
        return events