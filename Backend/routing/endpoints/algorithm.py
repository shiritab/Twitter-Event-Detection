from flask import Blueprint, Flask, jsonify, request, Response
import csv
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
import json
from operator import itemgetter
from ...algorithms.sedtwik.SedTwik import SedTwik
from ...algorithms.twembed.Twembeddings import Twembeddings
from ...algorithms.bert_topic.bert import Bert
from ...algorithms.eventDetectionAlgorithms import eventDetectionAlgorithms
from werkzeug.utils import secure_filename
import tempfile

# Do not delete this line
algorithm = Blueprint("algorithm", __name__)

####
algorithms_object = eventDetectionAlgorithms()
algorithms_object.add_algorithm("Bert",Bert())
algorithms_object.add_algorithm("SedTwik",SedTwik())
algorithms_object.add_algorithm("Twembeddings",Twembeddings())

TAGGED_TWEETS_PATH = f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv'
FILE_PATH = TAGGED_TWEETS_PATH
RELEVANT_TWEETS_PATH = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\data\relevant_tweets.tsv"
ALGORITHM_FILE = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\2012-10-12_{}.json"

@algorithm.route("/<algorithm>")
def run_algorithm(algorithm):
    return jsonify(algorithms_object.get_algorithms()[algorithm].run_algorithm(FILE_PATH))

@algorithm.route("/upload-data")
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        print(file.stream)
        temp = tempfile.TemporaryFile()
        stream = file.stream
        stream.seek(0)
        data = stream.read()
        print(data)

        my_json = data.decode('utf8').replace("'", '"')
        print(my_json)
        print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        with open('testttttttttt.json', 'w') as outfile:
            json.dump(my_json, outfile)
        with open('testttttttttt.json') as json_file:
            data = json.load(json_file)
            print(data)  # with open(file) as f:
        #
        # file.save(os.path.join('/',filename),500)
        a = "uploaded"

    return jsonify([{"hey": "hadassa"}])




@algorithm.route("/compare")
def compare_algorithms():
    list_output = []
    algorithms = algorithms_object.get_algorithms().keys()
    for algorithm in algorithms:
        dict_output = {}
        dict_output["name"] = algorithm
        tweets_dict = convert_results_to_vector(ALGORITHM_FILE.format(algorithm.lower()))
        lables, prediction = convert_tags_to_vector(tweets_dict)
        dict_output["data"] = [normalized_mutual_info_score(lables, prediction), adjusted_rand_score(lables, prediction)]

        print(normalized_mutual_info_score(lables, prediction))
        print(adjusted_rand_score(lables, prediction))
        list_output.append(dict_output)

    return jsonify(list_output)


def convert_tags_to_vector(tweets_dict):
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
    print(len(prediction))
    print(len(lable))
    return lable, prediction

def convert_results_to_vector(path):
    # TODO: adapt to changing algorithm
    f = open(path)
    tweets_dict = {}
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
    return tweets_dict

    # Closing file
    f.close()
