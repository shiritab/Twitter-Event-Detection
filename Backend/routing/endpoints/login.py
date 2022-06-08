import json
from flask import Blueprint, jsonify, request
from .algorithm import algorithms_object
# Do not delete this line
login = Blueprint("login", __name__)
####


@login.route("/")
def login_user():
    print("hello")
    print(request)
    print(request.data)
    return jsonify({"name":"hadassa"})
