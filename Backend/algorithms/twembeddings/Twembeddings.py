from . import *

class Twembeddings(DetectionAlgorithm):
    def __init__(self):
        super().__init__()

    def run_algorithm(self, *data):
        main({'model': ['tfidf_all_tweets'],
              'dataset': 'data/event2012json_2.tsv',
              'lang': 'en',
              'annotation': 'no',
              'threshold': ['0.7'],
              'batch_size': None,
              'remove_mentions': None,
              'window': 24})

        sort_results_by_cluster("data/event2012json_2_results.tsv")