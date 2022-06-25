import json
from flask import Blueprint, jsonify
from .algorithm import algorithms_object
# Do not delete this line
events = Blueprint("events", __name__)
####


@events.route("/summary/<algorithm>")
def get_algorithm_summary(algorithm):
    '''
    Given algorithm,
    applying summarize method over algorithm's object and returns results
    :param algorithm - string
    :return summarization - json
    '''
    return jsonify(algorithms_object.get_algorithms()[algorithm].summarize())
