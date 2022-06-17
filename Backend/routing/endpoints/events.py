import json
from flask import Blueprint, jsonify
from .algorithm import algorithms_object
# Do not delete this line
events = Blueprint("events", __name__)
####


@events.route("/summary/<algorithm>")
def get_algorithm_summary(algorithm):
    return jsonify(algorithms_object.get_algorithms()[algorithm].summarize())
