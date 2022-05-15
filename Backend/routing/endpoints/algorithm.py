from flask import Blueprint, Flask, jsonify, request
import csv
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
import json
from operator import itemgetter
from ...algorithms.sedtwik.SedTwik import SedTwik
from ...algorithms.eventDetectionAlgorithms import eventDetectionAlgorithms

# Do not delete this line
algorithm = Blueprint("algorithm", __name__)

####
algorithms_object = eventDetectionAlgorithms()
algorithms_object.add_algorithm("SedTwik", SedTwik())
tagged_tweets = f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv'

@algorithm.route("/<algorithm>")
def run_algorithm(algorithm):
    return jsonify(algorithms_object.get_algorithms()[algorithm].run_algorithm())

@algorithm.route("/compare")
def compare_algorithms():
    # TODO: shall refix this get request.
    tweets_dict = {}
    prediction = convert_results_to_vector()
    lables, prediction = convert_tags_to_vector()
    print(normalized_mutual_info_score(lables, prediction))
    print(adjusted_rand_score(lables, prediction))

def convert_tags_to_vector():
    tsv_file = open("relevant_tweets.tsv") # contains only 2 cols - cluster id, tweet id
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
    print(len(prediction))
    print(len(lable))
    return lable, prediction

def convert_results_to_vector(path):
    # TODO: adapt to changing algorithm
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    counter = 1
    list_pred = []
    for i in data:
        for tweet in i["tweets"]:
            tweets_dict[tweet] = counter
            list_pred.append([counter, tweet])
        counter += 1
    list_pred = sorted(list_pred, key=itemgetter(1))
    lable_pred = [x[0] for x in list_pred]
    print(len(lable_pred))
    return lable_pred

    # Closing file
    f.close()
