from flask import Blueprint, Flask, jsonify, request, Response
import csv
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
import json
from operator import itemgetter
from ...algorithms.sedtwik.SedTwik import SedTwik
from ...algorithms.twembeddings.Twembeddings import Twembeddings
from ...algorithms.bert_topic.bert import Bert
from ...algorithms.eventDetectionAlgorithms import eventDetectionAlgorithms
from werkzeug.utils import secure_filename
import tempfile

# Do not delete these lines
algorithm = Blueprint("algorithm", __name__)

algorithms_object = eventDetectionAlgorithms()
# saving each algorithm example
# algorithms_object.add_algorithm("Bert",Bert())
# algorithms_object.add_algorithm("SedTwik",SedTwik())
# algorithms_object.add_algorithm("Twembeddings",Twembeddings())

RELEVANT_TWEETS_PATH = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\data\relevant_tweets.tsv"
ALGORITHM_FILE = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\{}\results_event2012.json"
###

@algorithm.route("/<algorithm>")
def run_algorithm(algorithm):
    """"
    Given algorithm, gets algorithm' object and runs it.
    :param algorithm : get the algorithm to be run as a parameter
    :return algorithm's results
    """
    file_name = request.args.get('dataset')
    return jsonify(algorithms_object.get_algorithms()[algorithm].run_algorithm(file_name))

@algorithm.route("/compare")
def compare_algorithms():
    '''
    Iterates over each saved algorithm and gets perfomance.
    uses two measurements - normalized_mutual_info_score, adjusted_rand_score.
    :return measurements results - list
    '''
    list_output = []
    algorithms = algorithms_object.get_algorithms().keys()
    for algorithm in algorithms:
        print(algorithm)
        dict_output = {}

        dict_output["name"] = algorithm
        tweets_dict = convert_results_to_vector(ALGORITHM_FILE.format(algorithm.lower()))
        lables, prediction = convert_tags_to_vector(tweets_dict)
        dict_output["data"] = [round(normalized_mutual_info_score(lables, prediction),3), round(adjusted_rand_score(lables, prediction),3)]

        list_output.append(dict_output)
    return jsonify(list_output)

@algorithm.route("/all")
def get_algorithms():
    '''
    Returns all saved algorithms' names
    '''
    algorithms = list(algorithms_object.get_algorithms().keys())
    return jsonify(algorithms)


def convert_tags_to_vector(tweets_dict):
    '''
    Given tweets' clusters,
    extratcs each tweet's cluster - prediction vs actual
    :param tweets_dict - dict
    :return - list, list - actual, prediction
    '''
    tsv_file = open(RELEVANT_TWEETS_PATH) # contains only 2 cols - cluster id, tweet id
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    ground_truth = []
    list_pred = []
    for row in read_tsv:
        if row[1] in tweets_dict.keys():
            ground_truth.append(row)
            list_pred.append([tweets_dict[row[1]], row[1]])
    list_pred = sorted(list_pred, key=itemgetter(1))
    ground_truth = sorted(ground_truth, key=itemgetter(1))
    lable = [x[0] for x in ground_truth]
    prediction = [x[0] for x in list_pred]

    return lable, prediction

def convert_results_to_vector(path):
    f = open(path)
    tweets_dict = {}
    data = json.load(f)

    # Iterating through the json
    counter = 1
    list_pred = []
    for i in data:
        for tweet in i["tweets"]:
            tweet=str(tweet)
            tweets_dict[tweet] = counter
            list_pred.append([counter, tweet])
        counter += 1
    list_pred = sorted(list_pred, key=itemgetter(1))
    return tweets_dict

    # Closing file
    f.close()
